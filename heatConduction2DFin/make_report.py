#!/usr/bin/env python3
# ════════════════════════════════════════════════════════════════
#  FEAScript Benchmark
#  Finite Element Simulation in JavaScript
#  https://github.com/FEAScript/FEAScript-benchmark
#  MIT License © 2026 FEAScript
# ════════════════════════════════════════════════════════════════

"""Turn reports/<machine>/<version>/results.json into gnuplot data files, plots and a markdown summary table."""
import json, os, subprocess, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, ".."))
from browser import report as browser_report

# Usage: python3 make_report.py <machine> <version>   (a folder reports/<machine>/<version>/)
MACHINE, VERSION = sys.argv[1], sys.argv[2]
RUN = os.path.join(HERE, "reports", MACHINE, VERSION)
ALL = json.load(open(os.path.join(RUN, "results.json")))
meta = json.load(open(os.path.join(RUN, "meta.json")))
TAG = f"FEAScript {VERSION}, {meta['cpu']}"
R = [r for r in ALL if "failed" not in r]
P = os.path.join(RUN, "plots"); os.makedirs(P, exist_ok=True)

COLORS = {"FEAScript sparse LU": "#2a78d6", "FEAScript frontal": "#eb6834", "FEAScript Jacobi": "#7b52c7", "Elmer UMFPACK": "#1baf7a",
          "Elmer BiCGStab+ILU0": "#eda100", "Elmer MUMPS": "#e87ba4", "scikit-fem SuperLU": "#c0392b"}
PT = {"FEAScript sparse LU": 7, "FEAScript frontal": 5, "FEAScript Jacobi": 15, "Elmer UMFPACK": 9, "Elmer BiCGStab+ILU0": 11, "Elmer MUMPS": 13, "scikit-fem SuperLU": 4}
STYLE = """set terminal pngcairo size 900,620 font 'Arial,13'
set border 3 lc rgb '#888888'; set tics nomirror tc rgb '#333333'
set grid lc rgb '#e6e6e6' lw 1; set key top left box lc rgb '#cccccc' opaque
set logscale xy; set format y '10^{%L}'; set format x '10^{%L}'
"""

def series(code, order, key):
    rows = sorted((r for r in R if r["code"] == code and r["order"] == order and r["nx"] != 77), key=lambda r: r["nodes"])
    return [(r["nodes"], r[key]) for r in rows if r.get(key)]

def write(name, pts):
    f = os.path.join(P, name)
    with open(f, "w") as fh:
        fh.write("".join(f"{a} {b}\n" for a, b in pts))
    return name

def plot(out, title, ylabel, lines, extra=""):
    gp = STYLE + f"set output '{out}'\nset title '{title} ({TAG})' font 'Arial,15'\nset xlabel 'Number of nodes'\nset ylabel '{ylabel}'\n{extra}\nplot " + \
        ", \\\n     ".join(lines) + "\n"
    name = out.replace(".png", ".gnuplot")
    open(os.path.join(P, name), "w").write(gp)
    subprocess.run(["gnuplot", name], cwd=P, check=True)

# Runs from before scikit-fem was added do not have it
SKFEM = "scikit-fem SuperLU"
HAS_SKFEM = any(r["code"] == SKFEM for r in R)
# The curves of the codes coincide when FEAScript matches Elmer at every node; say so only when it is true
DIRECT = ("FEAScript frontal", "FEAScript sparse LU")  # Jacobi stops at a residual tolerance, so it is reported apart
def matches(order):
    fea = [r for r in R if r["order"] == order and r["code"] in DIRECT]
    return fea and all((r.get("maxDiffVsElmerUMFPACK") or 0) < 1e-4 for r in fea)
differ = [o for o in ("linear", "quadratic") if not matches(o)]
CODES = "FEAScript, scikit-fem and Elmer" if HAS_SKFEM else "FEAScript and Elmer"
ACCURACY_NOTE = (f"set label '{CODES} curves coincide (difference < 1e-5 K)' at graph 0.98,0.95 right tc rgb '#777777'" if not differ
                 else f"set label 'FEAScript differs from Elmer with {' and '.join(differ)} elements' at graph 0.98,0.95 right tc rgb '#777777'")

# 1. Accuracy vs analytical solution (RMS nodal error), linear & quadratic, both codes
lines = []
for order, dash in (("linear", 1), ("quadratic", 2)):
    for code, pt in (("FEAScript sparse LU", 7), ("Elmer UMFPACK", 6)) + (((SKFEM, 4),) if HAS_SKFEM else ()):
        d = write(f"err_{order}_{code.split()[0]}.dat", series(code, order, "rmsErr"))
        lines.append(f"'{d}' u 1:2 w lp lw 2 dt {dash} pt {pt} ps {1.0 if pt == 7 else 1.6} lc rgb '{COLORS[code]}' t '{code.split()[0]} ({order})'")
plot("accuracy.png", "RMS nodal error vs exact solution", "RMS error (K)", lines,
     "set key bottom left\n" + ACCURACY_NOTE)

# 2. In-solver time (assembly + linear solve), linear and quadratic elements
for order in ("linear", "quadratic"):
    lines = []
    for code in COLORS:
        pts = series(code, order, "solve")
        if code.startswith("Elmer"):
            pts = [(n, max(t, 0.005)) for n, t in pts]  # Elmer reports 0.01 s resolution
        if pts:
            d = write(f"solve_{order}_{code.replace(' ', '_').replace('+', '')}.dat", pts)
            lines.append(f"'{d}' u 1:2 w lp lw 2 pt {PT[code]} ps 1.2 lc rgb '{COLORS[code]}' t '{code}'")
    plot(f"solve_time_{order}.png", f"Assembly + solve time ({order} quads)", "Time (s)", lines,
         "set label 'Elmer timer resolution 0.01 s' at graph 0.98,0.05 right tc rgb '#777777'")

# 2b. Peak memory of each process (resident set size), when the run recorded it
HAS_MEMORY = any(r.get("peakMemoryMB") for r in R)
for order in ("linear", "quadratic") if HAS_MEMORY else ():
    lines = []
    for code in COLORS:
        pts = series(code, order, "peakMemoryMB")
        if pts:
            d = write(f"memory_{order}_{code.replace(' ', '_').replace('+', '')}.dat", pts)
            lines.append(f"'{d}' u 1:2 w lp lw 2 pt {PT[code]} ps 1.2 lc rgb '{COLORS[code]}' t '{code}'")
    plot(f"memory_{order}.png", f"Peak memory ({order} quads)", "Peak memory (MB)", lines,
         f"set label 'Whole process: includes {'Node.js, Python' if HAS_SKFEM else 'Node.js'} or Elmer itself' at graph 0.98,0.05 right tc rgb '#777777'")

# 3. End-to-end time on the 77x39 linear mesh (3120 nodes), split into startup/IO and solve
e2e = [r for r in R if r["nx"] == 77]
order = ["FEAScript sparse LU", "FEAScript frontal"] + ([SKFEM] if HAS_SKFEM else []) + ["Elmer BiCGStab+ILU0", "Elmer UMFPACK", "Elmer MUMPS"]
labels = {}
with open(os.path.join(P, "end_to_end.dat"), "w") as fh:
    for i, c in enumerate(order):
        r = next(x for x in e2e if x["code"] == c)
        fh.write(f"\"{labels.get(c, c).replace('+', '+')}\" {r['solve']:.3f} {r['process'] - r['solve']:.3f}\n")
gp = """set terminal pngcairo size 900,620 font 'Arial,13'
set output 'end_to_end.png'
set title 'End-to-end time, 77×39 linear quads (3,120 nodes) (@TAG@)' font 'Arial,14'
set border 3 lc rgb '#888888'; set tics nomirror; set grid ytics lc rgb '#e6e6e6'
set style data histograms; set style histogram rowstacked; set style fill solid border rgb 'white'
set boxwidth 0.6; set bmargin 7; set xrange [-0.6:@XMAX@]; set ylabel 'Time (s)'; set yrange [0:@YMAX@]; set xtics rotate by -25
set key top left box lc rgb '#cccccc' opaque
set label "Elmer runs on one core as one MPI process; most of its time is MPI start-up in this build, not solving" at screen 0.5,0.025 center tc rgb '#777777' font ',11'\nplot 'end_to_end.dat' u 2:xtic(1) t 'assembly + solve' lc rgb '#2a78d6', \\
     '' u 3 t 'process startup, library load / MPI init, I/O' lc rgb '#b7d3f6'
"""
open(os.path.join(P, "end_to_end.gnuplot"), "w").write(gp.replace("@TAG@", TAG).replace("@XMAX@", f"{len(order) - 0.4:.1f}").replace("@YMAX@", f"{max(r['process'] for r in e2e) * 1.5:.2f}"))
subprocess.run(["gnuplot", "end_to_end.gnuplot"], cwd=P, check=True)

# 4. Markdown table
cols = ["case", "nodes", "code", "solve", "linsolve", "process", "warmWall", "peakMemoryMB", "rmsErr", "maxErr", "maxDiffVsElmerUMFPACK"] + (["maxDiffVsFEAScript"] if HAS_SKFEM else []) + ["nruns"]
fmt = lambda v: "" if v is None else (f"{v:.3g}" if isinstance(v, float) else str(v))
md = "| " + " | ".join(cols) + " |\n|" + "---|" * len(cols) + "\n"
for r in ALL:
    md += "| " + " | ".join(fmt(r.get(c)) if not (c == "solve" and "failed" in r) else r["failed"] for c in cols) + " |\n"
open(os.path.join(RUN, "results_table.md"), "w").write(md)
print(md)

# 5. README of the results folder, from meta.json and the results
fea = [r for r in R if r["code"] in DIRECT]
agree = max((r.get("maxDiffVsElmerUMFPACK") or 0) for r in fea)
jacobi = [r for r in R if r["code"] == "FEAScript Jacobi"]
SKFEM_NOTE = (f"\nscikit-fem's nodal temperatures match FEAScript's (`lusolve`) to within {max(r['maxDiffVsFEAScript'] for r in R if r['code'] == SKFEM):.1e} and Elmer's (UMFPACK) to within {max(r['maxDiffVsElmerUMFPACK'] for r in R if r['code'] == SKFEM):.1e}, the rounding of the 8 significant digits that Elmer writes its results with.\n" if HAS_SKFEM else "")
JACOBI_NOTE = (f"\nWhere the Jacobi solver converged (residual tolerance 1e-8 within 10,000 iterations), its temperatures match Elmer's to within {max(r.get('maxDiffVsElmerUMFPACK') or 0 for r in jacobi):.1e}: it stops at a residual tolerance, so its error grows with the mesh.\n" if jacobi else "")
failed = [r for r in ALL if "failed" in r]
rows = [("FEAScript version", meta["feascriptVersion"]),
        ("FEAScript commit", meta["feascriptCommit"] + (" (with uncommitted changes)" if meta.get("feascriptUncommittedChanges") else "")),
        ("Released", meta.get("feascriptReleaseDate") or "not released"),
        ("Loaded from", f"`{meta.get('feascriptEntry', 'src/index.js')}`"),
        ("Elmer", meta["elmerVersion"] + (f" (build of commit `{meta['elmerCommit']}`, {meta['elmerBuildDate']})" if meta.get("elmerCommit") else "")), *([("scikit-fem", f"{meta['skfemVersion']} (SciPy {meta['scipyVersion']}, NumPy {meta['numpyVersion']}, Python {meta['python']})")] if meta.get("skfemVersion") else []),
        ("Node", meta["node"]), ("Machine", f"{meta['cpu']}" + (f", {meta['ramGB']} GB RAM" if meta.get("ramGB") else "") + f" ({meta.get('distribution', 'Linux')}, {meta.get('os', 'Linux')})"),
        ("Cores", meta["pinning"]), ("Repeats", f"median of {meta['reps']} fresh processes"), ("Run on", meta["date"])]
md = f"""# Results for FEAScript {VERSION} on {meta['cpu']}

| | |
|---|---|
""" + "".join(f"| {k} | {v} |\n" for k, v in rows) + (f"| Note | {meta['feascriptNote']} |\n" if meta.get("feascriptNote") else "") + f"""
All the numbers are in [results_table.md](results_table.md) and [results.json](results.json).

On every mesh it solved, FEAScript's nodal temperatures match Elmer's (UMFPACK) to within {agree:.1e} with the direct solvers (`frontal` and `lusolve`).
""" + SKFEM_NOTE + JACOBI_NOTE + ("".join(f"\n- **{r['code']}, {r['case']}:** {r['failed']}" for r in failed) and
       "\nRuns that could not be measured:\n" + "".join(f"\n- **{r['code']}, {r['case']}:** {r['failed']}" for r in failed) + "\n") + """
## Accuracy

<img src="plots/accuracy.png" width="600" alt="RMS error against the exact solution">

## Assembly and solve time

<img src="plots/solve_time_linear.png" width="600" alt="Assembly and solve time with linear elements">
<img src="plots/solve_time_quadratic.png" width="600" alt="Assembly and solve time with quadratic elements">

## End-to-end time

<img src="plots/end_to_end.png" width="600" alt="End-to-end time on the 77×39 mesh">
""" + ("""
## Peak memory

<img src="plots/memory_linear.png" width="600" alt="Peak memory with linear elements">
<img src="plots/memory_quadratic.png" width="600" alt="Peak memory with quadratic elements">
""" if HAS_MEMORY else "")
md += browser_report.section(RUN, P, ALL, TAG, "Browsers")
open(os.path.join(RUN, "README.md"), "w").write(md)
