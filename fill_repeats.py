#!/usr/bin/env python3
# ════════════════════════════════════════════════════════════════
#  FEAScript Benchmark
#  Finite Element Simulation in JavaScript
#  https://github.com/FEAScript/FEAScript-benchmark
#  MIT License © 2026 FEAScript
# ════════════════════════════════════════════════════════════════

"""Fill the Node.js repeated solves of a report that has none, without rerunning the rest.

Until November 2026, a FEAScript case with a first solve over 20 s was timed once, without repeated solves. Such a
case now gets one repeated solve, in a run of its own, as in the browsers. This adds it to an existing report:

    FEASCRIPT_CORE=<core at the report's feascriptCommit> FEASCRIPT_VERSION=<version> \\
        ~/.venvs/feascript-benchmark/bin/python fill_repeats.py <benchmark>

Use a FEAScript-core checkout (or `git archive`) of the commit in the report's meta.json, run on an otherwise idle
machine, then regenerate the report with `make_report.py <machine> <version>` in the benchmark folder.
"""
import importlib.util, json, os, statistics, sys

folder = os.path.abspath(sys.argv[1])
os.chdir(folder)
sys.path[:0] = [folder, os.path.dirname(folder)]
spec = importlib.util.spec_from_file_location("bench", os.path.join(folder, "benchmark.py"))
B = importlib.util.module_from_spec(spec)
spec.loader.exec_module(B)

report = os.path.join(B.RUN, "results.json")
node_path = os.path.join(B.FEA_OUT, "results.json")
results, node_rows = json.load(open(report)), json.load(open(node_path))


def gaps():
    return [r for r in results if "failed" not in r and r["code"].startswith("FEAScript") and r.get("warmWall") is None]


print(f"{os.path.basename(folder)} {B.VERSION} on {B.MACHINE}: {len(gaps())} gaps, core {B.CORE}", flush=True)
for r in gaps():
    try:
        if "nx" in r and "ny" in r:  # heatConduction2DFin
            out = B.run_fea(r["order"], r["nx"], r["ny"], B.FEA_CFGS[r["code"]], warm=1)
        elif "shape" in r:  # heatConduction2DFinGmsh
            out = B.run_fea(os.path.join(B.GMSH_MESHES, f"{r['case']}.msh"), B.FEA_CFGS[r["code"]], warm=1)
        else:  # creepingFlow2DLidDrivenCavity
            out = B.run_fea(r["n"], warm=1)
    except RuntimeError as e:
        print(f"{r['case']} {r['code']}: failed, {str(e)[:300]}", flush=True)
        continue
    r["warmWall"] = statistics.median(out["warm"])
    for n in node_rows:
        if n["case"] == r["case"] and n["code"] == r["code"]:
            n["warmWall"] = r["warmWall"]
    print(f"{r['case']} {r['code']}: first solve {out['coldWall']:.2f} s (report {r['solve']:.2f} s), repeated solve {r['warmWall']:.2f} s", flush=True)
    for path, rows in ((report, results), (node_path, node_rows)):
        with open(path, "w") as f:
            json.dump(rows, f, indent=1)
left = gaps()
print("no gaps left" if not left else "gaps left: " + ", ".join(f"{r['code']} {r['case']}" for r in left), flush=True)
