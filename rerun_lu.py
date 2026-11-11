#!/usr/bin/env python3
# ════════════════════════════════════════════════════════════════
#  FEAScript Benchmark
#  Finite Element Simulation in JavaScript
#  https://github.com/FEAScript/FEAScript-benchmark
#  MIT License © 2026 FEAScript
# ════════════════════════════════════════════════════════════════

"""Rerun the sparse LU (lusolve) cases of a report, in Node.js and the browsers, without rerunning the rest.

Used for the fix of FEAScript-core issue #136 in 0.4.0: the bundle's sparse LU changed, its results did not.

    FEASCRIPT_CORE=<core with the new bundle> FEASCRIPT_VERSION=<version> FEASCRIPT_NOTE="<note for the report>" \\
        ~/.venvs/feascript-benchmark/bin/python rerun_lu.py <benchmark>

Every new solution must be the same, bit for bit, as the one stored by the report run; the script stops if not.
Run on an otherwise idle machine, then regenerate the report with `make_report.py <machine> <version>` in the
benchmark folder.
"""
import filecmp, importlib.util, json, os, statistics, sys, tempfile

folder = os.path.abspath(sys.argv[1])
os.chdir(folder)
sys.path[:0] = [folder, os.path.dirname(folder)]
spec = importlib.util.spec_from_file_location("bench", os.path.join(folder, "benchmark.py"))
B = importlib.util.module_from_spec(spec)
spec.loader.exec_module(B)
from browser import runner as browser_runner

CODE = "FEAScript sparse LU"
report = os.path.join(B.RUN, "results.json")
node_path = os.path.join(B.FEA_OUT, "results.json")
results, node_rows = json.load(open(report)), json.load(open(node_path))
rows = [r for r in results if r["code"] == CODE and "failed" not in r]
print(f"{os.path.basename(folder)} {B.VERSION} on {B.MACHINE}: {len(rows)} sparse LU cases, core {B.CORE}", flush=True)


def fea(r, csv=None, warm=0):
    if "nx" in r and "ny" in r:
        return B.run_fea(r["order"], r["nx"], r["ny"], "lusolve", csv, warm=warm)
    if "shape" in r:
        return B.run_fea(os.path.join(B.GMSH_MESHES, f"{r['case']}.msh"), "lusolve", csv, warm=warm)
    return B.run_fea(r["n"], csv, warm=warm)


def stored_csv(r):
    plain = "nx" not in r and "shape" not in r  # the cavity names its results by the mesh only
    return os.path.join(B.FEA_OUT, f"{r['case']}.csv" if plain else f"lusolve_{r['case']}.csv")


if not os.environ.get("ONLY_BROWSERS"):
    with tempfile.TemporaryDirectory() as tmp:
        for r in rows:
            csv = os.path.join(tmp, "solution.csv")
            first = fea(r, csv)
            if not filecmp.cmp(csv, stored_csv(r), shallow=False):
                sys.exit(f"{r['case']}: the solution differs from the stored one")
            if first["coldWall"] > 20:  # timed once, with one repeated solve in a run of its own
                first["warm"] = fea(r, warm=1)["warm"]
                runs = [first]
            else:
                warm = fea(r, warm=B.WARM)
                first["warm"] = warm["warm"]
                warm["process"] = None  # includes the repeated solves, so not an end-to-end time
                runs = [first, warm] + [fea(r) for _ in range(B.REPS - 2)]
            keep = [x for x in runs if x["process"] is not None]
            new = {"solve": statistics.median(x["coldWall"] for x in runs),
                   "linsolve": statistics.median(x["coldSystem"] or 0 for x in runs),
                   "process": statistics.median(x["process"] for x in keep),
                   "peakMemoryMB": statistics.median(x["peakMemory"] for x in keep),
                   "warmWall": statistics.median(first["warm"]) if first["warm"] else None, "nruns": len(runs)}
            print(f"{r['case']}: first solve {r['solve']:.2f} -> {new['solve']:.2f} s, repeated "
                  f"{r.get('warmWall') or 0:.2f} -> {new['warmWall'] or 0:.2f} s", flush=True)
            for target in [r] + [n for n in node_rows if n["case"] == r["case"] and n["code"] == CODE]:
                target.update({k: v for k, v in new.items()}, **({"wall": new["solve"]} if "wall" in target else {}))
            for path, data in ((report, results), (node_path, node_rows)):
                with open(path, "w") as f:
                    json.dump(data, f, indent=1)

if not os.environ.get("NO_BROWSERS"):
    cases = [c for c in B.browser_cases() if c["code"] == CODE]
    browser_runner.run_cases(cases, os.path.join(folder, "feascript", "case.mjs"), B.CORE, B.RUN, B.FEA_RESULTS, B.PIN, B.REPS, B.WARM,
                             getattr(B, "GMSH_MESHES", None))

if os.environ.get("FEASCRIPT_NOTE"):
    meta_path = os.path.join(B.RUN, "meta.json")
    meta = json.load(open(meta_path))
    meta["feascriptNote"] = os.environ["FEASCRIPT_NOTE"]
    with open(meta_path, "w") as f:
        json.dump(meta, f, indent=1)
