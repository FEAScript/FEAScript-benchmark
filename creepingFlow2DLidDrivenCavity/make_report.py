#!/usr/bin/env python3
# ════════════════════════════════════════════════════════════════
#  FEAScript Benchmark
#  Finite Element Simulation in JavaScript
#  https://github.com/FEAScript/FEAScript-benchmark
#  MIT License © 2026 FEAScript
# ════════════════════════════════════════════════════════════════

"""Turn results/<machine>/<version>/results.json into plots, a results table and a README.

Usage: python3 make_report.py <machine> <version>
"""
import json, os, re, subprocess, sys
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
MACHINE, VERSION = sys.argv[1], sys.argv[2]
RUN = os.path.join(HERE, "results", MACHINE, VERSION)
ALL = json.load(open(os.path.join(RUN, "results.json")))
R = [r for r in ALL if "failed" not in r]
META = json.load(open(os.path.join(RUN, "meta.json")))
P = os.path.join(RUN, "plots"); os.makedirs(P, exist_ok=True)

COLORS = {"FEAScript sparse LU": "#2a78d6", "Elmer UMFPACK": "#1baf7a", "Elmer MUMPS": "#e87ba4"}
PT = {"FEAScript sparse LU": 7, "Elmer UMFPACK": 9, "Elmer MUMPS": 13}
STYLE = """set terminal pngcairo size 900,620 font 'Arial,13'
set border 3 lc rgb '#888888'; set tics nomirror tc rgb '#333333'
set grid lc rgb '#e6e6e6' lw 1; set key top left box lc rgb '#cccccc' opaque
"""
TITLE = f"(FEAScript {VERSION}, {META['cpu']})"


def series(code, key):
    return sorted((r["nodes"], r[key], r["n"]) for r in R if r["code"] == code and r.get(key) is not None)


def tag(code):
    return re.sub(r"\W+", "_", code)


def gnuplot(name, body):
    open(os.path.join(P, f"{name}.gnuplot"), "w").write(STYLE + f"set output '{name}.png'\n" + body)
    subprocess.run(["gnuplot", f"{name}.gnuplot"], cwd=P, check=True)


# 1. Assembly + solve time against the number of nodes
lines = []
for code in COLORS:
    pts = [(nodes, max(t, 0.005)) for nodes, t, _ in series(code, "solve")]  # Elmer reports 0.01 s resolution
    if pts:
        np.savetxt(os.path.join(P, f"solve_{tag(code)}.dat"), pts)
        lines.append(f"'solve_{tag(code)}.dat' u 1:2 w lp lw 2 pt {PT[code]} ps 1.2 lc rgb '{COLORS[code]}' t '{code}'")
gnuplot("solve_time", f"""set title 'Assembly + solve time {TITLE}' font 'Arial,15'
set logscale xy; set format y '10^{{%L}}'; set format x '10^{{%L}}'
set xlabel 'Number of nodes (Q2 velocity nodes)'; set ylabel 'Time (s)'
set label 'Elmer timer resolution 0.01 s' at graph 0.98,0.05 right tc rgb '#777777'
plot """ + ", \\\n     ".join(lines) + "\n")

# 2. Primary vortex strength (minimum of the stream function) against the mesh
lines = []
for code in ["FEAScript sparse LU", "Elmer UMFPACK"]:
    pts = [(n, psi) for _, psi, n in series(code, "psiMin")]
    np.savetxt(os.path.join(P, f"psi_{tag(code)}.dat"), pts)
    lines.append(f"'psi_{tag(code)}.dat' u 1:2 w lp lw 2 pt {PT[code]} ps {1.6 if 'Elmer' in code else 1.0} lc rgb '{COLORS[code]}' t '{code.split()[0]}'")
gnuplot("psi_min", f"""set title 'Primary vortex strength ψ_{{min}} {TITLE}' font 'Arial,15'
set logscale x 2; set xlabel 'Elements per side n (n × n mesh)'; set ylabel 'ψ_{{min}}'
set key top right
plot """ + ", \\\n     ".join(lines) + "\n")

# 3. Centerline velocity u(0.5, y) on the finest mesh that both codes solved
both = sorted({r["n"] for r in R if r["code"] == "FEAScript sparse LU"} & {r["n"] for r in R if r["code"] == "Elmer UMFPACK"})
nmax = both[-1]
lines = [f"'../work/centerline_{tag(code)}_{nmax}x{nmax}.dat' u 2:1 w {'l lw 3' if 'Elmer' in code else 'p pt 7 ps 0.6'} lc rgb '{COLORS[code]}' t '{code.split()[0]}'"
         for code in ["Elmer UMFPACK", "FEAScript sparse LU"]]
gnuplot("centerline", f"""set title 'Velocity u along the vertical centerline, {nmax}×{nmax} mesh {TITLE}' font 'Arial,14'
set xlabel 'u(0.5, y)'; set ylabel 'y'; set yrange [0:1]; set key bottom right
plot """ + ", \\\n     ".join(lines) + "\n")

# 4. End-to-end time on the 16x16 mesh, split into startup/IO and solve
e2e = [r for r in R if r["n"] == 16]
with open(os.path.join(P, "end_to_end.dat"), "w") as fh:
    for code in COLORS:
        r = next((x for x in e2e if x["code"] == code), None)
        if r:
            fh.write(f"\"{code}\" {r['solve']:.3f} {r['process'] - r['solve']:.3f}\n")
ymax = max(r["process"] for r in e2e) * 1.5
gnuplot("end_to_end", f"""set title 'End-to-end time, 16×16 mesh {TITLE}' font 'Arial,15'
set grid ytics; set style data histograms; set style histogram rowstacked; set style fill solid border rgb 'white'
set label "Elmer runs on one core as one MPI process; most of its time is MPI start-up in this build, not solving" at screen 0.5,0.025 center tc rgb '#777777' font ',11'
set boxwidth 0.6; set bmargin 5; set xrange [-0.6:2.6]; set ylabel 'Time (s)'; set yrange [0:{ymax:.2f}]; set key top left box
plot 'end_to_end.dat' u 2:xtic(1) t 'assembly + solve' lc rgb '#2a78d6', \\
     '' u 3 t 'process startup, library load / MPI init, I/O' lc rgb '#b7d3f6'
""")

# 5. Results table
cols = ["case", "nodes", "code", "solve", "linsolve", "process", "warmWall", "psiMin", "psiMinY",
        "maxDiffVelocity", "maxDiffVelocityAwayFromCorners", "nruns"]
fmt = lambda v: "" if v is None else (f"{v:.4g}" if isinstance(v, float) else str(v))
md = "| " + " | ".join(cols) + " |\n|" + "---|" * len(cols) + "\n"
for r in ALL:
    md += "| " + " | ".join(r["failed"] if (c == "solve" and "failed" in r) else fmt(r.get(c)) for c in cols) + " |\n"
open(os.path.join(RUN, "results_table.md"), "w").write(md)

# 6. README of the results folder
fea = [r for r in R if r["code"] == "FEAScript sparse LU"]
psi_diff = max(abs(r["psiMin"] - next(e["psiMin"] for e in R if e["code"] == "Elmer UMFPACK" and e["n"] == r["n"])) for r in fea)
fea_by_n = sorted(fea, key=lambda r: r["n"])
coarse, fine = fea_by_n[0], fea_by_n[-1]
# Say that the codes converge to the same solution only when the difference keeps shrinking with the mesh
if fine["maxDiffVelocityAwayFromCorners"] < coarse["maxDiffVelocityAwayFromCorners"] / 10:
    CONVERGENCE = ", so both converge to the same solution."
else:
    CONVERGENCE = (": the difference does not shrink as the mesh is refined, so the two codes do not converge to the same "
                   "solution." + (" In FEAScript releases before 0.4.0, the moving lid also set the velocity of one of its "
                                  "corner nodes, so fluid leaked through the side wall there; this was fixed in 0.4.0."
                                  if re.match(r"0\.[0-3]\.", VERSION) else ""))
failed = [r for r in ALL if "failed" in r]
rows = [("FEAScript version", META["feascriptVersion"]),
        ("FEAScript commit", META["feascriptCommit"] + (" (with uncommitted changes)" if META.get("feascriptUncommittedChanges") else "")),
        ("Released", META.get("feascriptReleaseDate") or "not released"),
        ("Loaded from", f"`{META['feascriptEntry']}`"), ("Elmer", META["elmerVersion"]), ("Node", META["node"]),
        ("Machine", f"{META['cpu']} ({META.get('os', '')})"), ("Cores", META["pinning"]),
        ("Repeats", f"median of {META['reps']} fresh processes"), ("Run on", META["date"])]
md = f"""# Results for FEAScript {VERSION} on {META['cpu']}

| | |
|---|---|
""" + "".join(f"| {k} | {v} |\n" for k, v in rows) + f"""
All the numbers are in [results_table.md](results_table.md) and [results.json](results.json).

On every mesh it solved, FEAScript's primary vortex strength ψ_min matches Elmer's (UMFPACK) to within {psi_diff:.1e}.

At the nodes farther than 0.2 from the two lid corners, the velocities of the two codes differ by at most {fine['maxDiffVelocityAwayFromCorners']:.1e} on the {fine['case'].replace('x', '×')} mesh, against {coarse['maxDiffVelocityAwayFromCorners']:.1e} on the {coarse['case'].replace('x', '×')} mesh{CONVERGENCE} Next to the lid corners they differ by up to {fine['maxDiffVelocity']:.2f} on every mesh: there FEAScript applies the full lid velocity along the top edge of the corner element, while Elmer interpolates it linearly from the corner, where the velocity is 0.
""" + ("\nRuns that could not be measured:\n" + "".join(f"\n- **{r['code']}, {r['case']}:** {r['failed']}" for r in failed) + "\n" if failed else "") + """
## Primary vortex strength

<img src="plots/psi_min.png" width="600" alt="Primary vortex strength against the mesh">

## Centerline velocity

<img src="plots/centerline.png" width="600" alt="Velocity along the vertical centerline">

## Assembly and solve time

<img src="plots/solve_time.png" width="600" alt="Assembly and solve time against the number of nodes">

## End-to-end time

<img src="plots/end_to_end.png" width="600" alt="End-to-end time on the 16×16 mesh">
"""
open(os.path.join(RUN, "README.md"), "w").write(md)
print(RUN)
