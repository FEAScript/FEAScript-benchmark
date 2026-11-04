#!/usr/bin/env python3
"""Turn results/results.json into gnuplot data files, plots and a markdown summary table."""
import json, os, subprocess, sys
HERE = os.path.dirname(os.path.abspath(__file__))
# Usage: python3 make_report.py <version>   (a folder under results/, e.g. 0.4.0-rc)
VERSION = sys.argv[1] if len(sys.argv) > 1 else sorted(d for d in os.listdir(os.path.join(HERE, "results")) if d != "meshes")[-1]
RUN = os.path.join(HERE, "results", VERSION)
ALL = json.load(open(os.path.join(RUN, "results.json")))
R = [r for r in ALL if "failed" not in r]
P = os.path.join(RUN, "plots"); os.makedirs(P, exist_ok=True)

COLORS = {"FEAScript sparse LU": "#2a78d6", "FEAScript frontal": "#eb6834", "Elmer UMFPACK": "#1baf7a",
          "Elmer BiCGStab+ILU0": "#eda100", "Elmer MUMPS": "#e87ba4"}
PT = {"FEAScript sparse LU": 7, "FEAScript frontal": 5, "Elmer UMFPACK": 9, "Elmer BiCGStab+ILU0": 11, "Elmer MUMPS": 13}
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
    gp = STYLE + f"set output '{out}'\nset title '{title} (FEAScript {VERSION})' font 'Arial,16'\nset xlabel 'Number of nodes'\nset ylabel '{ylabel}'\n{extra}\nplot " + \
        ", \\\n     ".join(lines) + "\n"
    name = out.replace(".png", ".gnuplot")
    open(os.path.join(P, name), "w").write(gp)
    subprocess.run(["gnuplot", name], cwd=P, check=True)

# 1. Accuracy vs analytical solution (RMS nodal error), linear & quadratic, both codes
lines = []
for order, dash in (("linear", 1), ("quadratic", 2)):
    for code, pt in (("FEAScript sparse LU", 7), ("Elmer UMFPACK", 6)):
        d = write(f"err_{order}_{code.split()[0]}.dat", series(code, order, "rmsErr"))
        c = COLORS["FEAScript sparse LU" if code.startswith("FEA") else "Elmer UMFPACK"]
        lines.append(f"'{d}' u 1:2 w lp lw 2 dt {dash} pt {pt} ps {1.6 if pt == 6 else 1.0} lc rgb '{c}' t '{code.split()[0]} ({order})'")
plot("accuracy.png", "RMS nodal error vs exact solution", "RMS error (K)", lines,
     "set label 'FEAScript and Elmer curves coincide (difference < 1e-5 K)' at graph 0.98,0.05 right tc rgb '#777777'")

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

# 3. Original case (77x39 linear, 3120 nodes): end-to-end process time split into startup/IO and solve
orig = [r for r in R if r["nx"] == 77]
order = ["FEAScript sparse LU", "FEAScript frontal", "Elmer BiCGStab+ILU0", "Elmer UMFPACK", "Elmer MUMPS"]
labels = {}
with open(os.path.join(P, "original_case.dat"), "w") as fh:
    for i, c in enumerate(order):
        r = next(x for x in orig if x["code"] == c)
        fh.write(f"\"{labels.get(c, c).replace('+', '+')}\" {r['solve']:.3f} {r['process'] - r['solve']:.3f}\n")
gp = """set terminal pngcairo size 900,620 font 'Arial,13'
set output 'original_case.png'
set title 'Original case, 77x39 linear quads (3120 nodes): end-to-end time (FEAScript @VERSION@)' font 'Arial,14'
set border 3 lc rgb '#888888'; set tics nomirror; set grid ytics lc rgb '#e6e6e6'
set style data histograms; set style histogram rowstacked; set style fill solid border rgb 'white'
set boxwidth 0.6; set bmargin 7; set xrange [-0.6:4.6]; set ylabel 'Time (s)'; set yrange [0:3.2]; set xtics rotate by -25
set key top left box lc rgb '#cccccc' opaque
plot 'original_case.dat' u 2:xtic(1) t 'assembly + solve' lc rgb '#2a78d6', \\
     '' u 3 t 'process startup, library load / MPI init, I/O' lc rgb '#b7d3f6'
"""
open(os.path.join(P, "original_case.gnuplot"), "w").write(gp.replace("@VERSION@", VERSION))
subprocess.run(["gnuplot", "original_case.gnuplot"], cwd=P, check=True)

# 4. Markdown table
cols = ["case", "nodes", "code", "solve", "linsolve", "process", "warmWall", "rmsErr", "maxErr", "maxDiffVsElmerUMFPACK", "nruns"]
fmt = lambda v: "" if v is None else (f"{v:.3g}" if isinstance(v, float) else str(v))
md = "| " + " | ".join(cols) + " |\n|" + "---|" * len(cols) + "\n"
for r in ALL:
    md += "| " + " | ".join(fmt(r.get(c)) if not (c == "solve" and "failed" in r) else r["failed"] for c in cols) + " |\n"
open(os.path.join(RUN, "results_table.md"), "w").write(md)
print(md)
