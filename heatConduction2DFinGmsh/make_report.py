#!/usr/bin/env python3
# ════════════════════════════════════════════════════════════════
#  FEAScript Benchmark
#  Finite Element Simulation in JavaScript
#  https://github.com/FEAScript/FEAScript-benchmark
#  MIT License © 2026 FEAScript
# ════════════════════════════════════════════════════════════════

"""Turn reports/<machine>/<version>/results.json into plots, a results table and a README.

Usage: python3 make_report.py <machine> <version>
"""
import json, os, re, subprocess, sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, ".."))
from browser import report as browser_report

MACHINE, VERSION = sys.argv[1], sys.argv[2]
RUN = os.path.join(HERE, "reports", MACHINE, VERSION)
ALL = json.load(open(os.path.join(RUN, "results.json")))
meta = json.load(open(os.path.join(RUN, "meta.json")))
TAG = f"FEAScript {VERSION}, {meta['cpu']}"
R = [r for r in ALL if "failed" not in r]
P = os.path.join(RUN, "plots"); os.makedirs(P, exist_ok=True)

COLORS = {"FEAScript sparse LU": "#2a78d6", "FEAScript frontal": "#eb6834", "Elmer UMFPACK": "#1baf7a", "scikit-fem SuperLU": "#c0392b", "scikit-fem fine integration": "#7b52c7"}
PT = {"FEAScript sparse LU": 7, "FEAScript frontal": 5, "Elmer UMFPACK": 9, "scikit-fem SuperLU": 4, "scikit-fem fine integration": 15}
SHAPES = {"tri": "triangles", "quad": "quadrilaterals"}
ORDERS = ("linear", "quadratic")
STYLE = """set terminal pngcairo size 900,620 font 'Arial,13'
set border 3 lc rgb '#888888'; set tics nomirror tc rgb '#333333'
set grid lc rgb '#e6e6e6' lw 1; set key top left box lc rgb '#cccccc' opaque
set logscale xy; set format y '10^{%L}'; set format x '10^{%L}'
"""


def series(code, shape, order, key):
    rows = sorted((r for r in R if r["code"] == code and r["shape"] == shape and r["order"] == order), key=lambda r: r["nodes"])
    return [(r["nodes"], r[key]) for r in rows if r.get(key) is not None]


def tag(text):
    return re.sub(r"\W+", "_", text)


def write(name, pts):
    with open(os.path.join(P, name), "w") as f:
        f.write("".join(f"{a} {b}\n" for a, b in pts))
    return name


def plot(out, title, ylabel, lines, extra=""):
    gp = STYLE + f"set output '{out}.png'\nset title '{title} ({TAG})' font 'Arial,14'\nset xlabel 'Number of nodes'\nset ylabel '{ylabel}'\n{extra}\nplot " + ", \\\n     ".join(lines) + "\n"
    with open(os.path.join(P, f"{out}.gnuplot"), "w") as f:
        f.write(gp)
    subprocess.run(["gnuplot", f"{out}.gnuplot"], cwd=P, check=True)


# 1. Accuracy against the exact solution, for each element shape
for shape, label in SHAPES.items():
    lines = []
    for order, dash in zip(ORDERS, (1, 2)):
        for code in ("FEAScript sparse LU", "Elmer UMFPACK", "scikit-fem SuperLU") + (("scikit-fem fine integration",) if shape == "quad" else ()):
            d = write(f"err_{shape}_{order}_{tag(code)}.dat", series(code, shape, order, "rmsErr"))
            name = code.replace(" sparse LU", "").replace(" UMFPACK", "").replace(" SuperLU", "")
            lines.append(f"'{d}' u 1:2 w lp lw 2 dt {dash} pt {PT[code]} ps {1.0 if code.startswith('FEA') else 1.6} lc rgb '{COLORS[code]}' t '{name} ({order})'")
    plot(f"accuracy_{shape}", f"RMS nodal error vs exact solution, {label}", "RMS error (K)", lines, "set key bottom left")

# 2. Assembly and solve time, and peak memory, for each kind of element
for shape, label in SHAPES.items():
    for order in ORDERS:
        for key, stem, ylabel, title, note in (
            ("solve", "solve_time", "Time (s)", "Assembly + solve time", "Elmer timer resolution 0.01 s"),
            ("peakMemoryMB", "memory", "Peak memory (MB)", "Peak memory", "Whole process: includes Node.js, Python or Elmer itself"),
        ):
            lines = []
            for code in ("FEAScript sparse LU", "FEAScript frontal", "Elmer UMFPACK", "scikit-fem SuperLU"):
                pts = [(n, max(v, 0.005)) for n, v in series(code, shape, order, key)]
                if pts:
                    d = write(f"{stem}_{shape}_{order}_{tag(code)}.dat", pts)
                    lines.append(f"'{d}' u 1:2 w lp lw 2 pt {PT[code]} ps 1.2 lc rgb '{COLORS[code]}' t '{code}'")
            plot(f"{stem}_{shape}_{order}", f"{title}, {order} {label}", ylabel, lines, f"set label '{note}' at graph 0.98,0.05 right tc rgb '#777777'")

# 3. Results table
cols = ["case", "nodes", "code", "solve", "linsolve", "process", "warmWall", "peakMemoryMB", "rmsErr", "maxErr", "maxDiffVsFEAScript", "nruns"]
fmt = lambda v: "" if v is None else (f"{v:.3g}" if isinstance(v, float) else str(v))
md = "| " + " | ".join(cols) + " |\n|" + "---|" * len(cols) + "\n"
for r in ALL:
    md += "| " + " | ".join(r["failed"] if (c == "solve" and "failed" in r) else fmt(r.get(c)) for c in cols) + " |\n"
open(os.path.join(RUN, "results_table.md"), "w").write(md)

# 4. README of the run
worst = lambda code, shape: max((r.get("maxDiffVsFEAScript") or 0) for r in R if r["code"] == code and r["shape"] == shape)
direct = max(worst("FEAScript frontal", s) for s in SHAPES)
elmer = max(worst("Elmer UMFPACK", s) for s in SHAPES)
matched = max(worst("scikit-fem SuperLU", s) for s in SHAPES)
gains = []
for r in R:
    if r["code"] == "scikit-fem fine integration" and r["shape"] == "quad":
        base = next(x for x in R if x["code"] == "FEAScript sparse LU" and x["case"] == r["case"])
        gains.append(100 * (base["rmsErr"] / r["rmsErr"] - 1))
failed = [r for r in ALL if "failed" in r]
rows = [("FEAScript version", meta["feascriptVersion"]),
        ("FEAScript commit", meta["feascriptCommit"] + (" (with uncommitted changes)" if meta.get("feascriptUncommittedChanges") else "")),
        ("Released", meta.get("feascriptReleaseDate") or "not released"), ("Loaded from", f"`{meta['feascriptEntry']}`"),
        ("Elmer", meta["elmerVersion"] + (f" (build of commit `{meta['elmerCommit']}`, {meta['elmerBuildDate']})" if meta.get("elmerCommit") else "")),
        ("scikit-fem", f"{meta['skfemVersion']} (SciPy {meta['scipyVersion']}, NumPy {meta['numpyVersion']}, meshio {meta['meshioVersion']}, Python {meta['python']})"),
        ("Gmsh", meta["gmshVersion"]), ("Node", meta["node"]),
        ("Machine", f"{meta['cpu']}, {meta['ramGB']} GB RAM ({meta['distribution']}, {meta['os']})"), ("Cores", meta["pinning"]),
        ("Repeats", f"median of {meta['reps']} fresh processes"), ("Run on", meta["date"])]
md = f"""# Results for FEAScript {VERSION} on {meta['cpu']}

| | |
|---|---|
""" + "".join(f"| {k} | {v} |\n" for k, v in rows) + f"""
All the numbers are in [results_table.md](results_table.md) and [results.json](results.json).

On every mesh it solved, with triangles and quadrilaterals, FEAScript's nodal temperatures match scikit-fem's to within {matched:.1e} when scikit-fem uses the same Gauss rules, and Elmer's (UMFPACK) to within {elmer:.1e}. The `frontal` and `lusolve` solvers agree to within {direct:.1e}.

On distorted quadrilaterals these Gauss rules are not exact. With a much finer rule, scikit-fem's RMS error is lower than FEAScript's by {min(gains):.1f}% to {max(gains):.1f}%. On triangles the rules are exact, so the finer rule changes nothing.
""" + ("\nRuns that could not be measured:\n" + "".join(f"\n- **{r['code']}, {r['case']}:** {r['failed']}" for r in failed) + "\n" if failed else "") + browser_report.no_repeat(ALL) + """
## Accuracy

<img src="plots/accuracy_tri.png" width="600" alt="RMS error against the exact solution on triangles">
<img src="plots/accuracy_quad.png" width="600" alt="RMS error against the exact solution on quadrilaterals">

## Assembly and solve time

""" + "".join(f'<img src="plots/solve_time_{s}_{o}.png" width="600" alt="Assembly and solve time, {o} {l}">\n' for s, l in SHAPES.items() for o in ORDERS) + """
## Peak memory

""" + "".join(f'<img src="plots/memory_{s}_{o}.png" width="600" alt="Peak memory, {o} {l}">\n' for s, l in SHAPES.items() for o in ORDERS)
md += browser_report.section(RUN, P, ALL, TAG, "Browsers")
open(os.path.join(RUN, "README.md"), "w").write(md)
print(RUN)
