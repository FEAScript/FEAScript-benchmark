#!/usr/bin/env python3
"""Plot FEAScript solve time across versions, from every results/<version>/ folder.

Usage: python3 make_history.py [--case linear-160x80]
Writes history/<case>.dat and history/<case>.png.
"""
import argparse, json, os, subprocess

HERE = os.path.dirname(os.path.abspath(__file__))
RESULTS = os.path.join(HERE, "results")
SOLVERS = [("FEAScript frontal", "frontal", "#eb6834"), ("FEAScript sparse LU", "sparse LU", "#2a78d6")]

ap = argparse.ArgumentParser()
ap.add_argument("--case", default="linear-160x80", help="mesh case, e.g. linear-160x80 or quadratic-80x40")
case = ap.parse_args().case

# Collect one row per version, ordered by run date
rows, metas = [], []
for version in os.listdir(RESULTS):
    run = os.path.join(RESULTS, version)
    if not os.path.isfile(os.path.join(run, "results.json")):
        continue
    meta = json.load(open(os.path.join(run, "meta.json")))
    recs = {r["code"]: r for r in json.load(open(os.path.join(run, "results.json"))) if r["case"] == case}
    if not recs:
        continue
    times = [recs.get(code, {}).get("solve") for code, _, _ in SOLVERS]
    nodes = next(r["nodes"] for r in recs.values() if "nodes" in r)
    rows.append((meta["date"], version, times))
    metas.append(meta)
rows.sort()
if not rows:
    raise SystemExit(f"No results for case {case}")

out = os.path.join(HERE, "history"); os.makedirs(out, exist_ok=True)
with open(os.path.join(out, f"{case}.dat"), "w") as f:
    f.write("# version date " + " ".join(label.replace(" ", "_") for _, label, _ in SOLVERS) + "  (assembly + solve, s; NaN = not run)\n")
    for date, version, times in rows:
        f.write(f"{version} {date} " + " ".join("NaN" if t is None else f"{t:.3f}" for t in times) + "\n")

order, (nx, ny) = case.split("-")[0], case.split("-")[1].split("x")
cpus = sorted({m["cpu"] for m in metas}); nodes_js = sorted({m["node"] for m in metas})
subtitle = (f"2D fin heat conduction, {nx}×{ny} {order} quads ({nodes:,} nodes) · "
            f"{', '.join(cpus)}, 1 core, Node {', '.join(nodes_js)}")
ymax = max(t for _, _, ts in rows for t in ts if t is not None) * 1.25

gp = f"""set terminal pngcairo size 900,600 font 'Arial,13'
set output '{case}.png'
set title "FEAScript assembly + solve time by version\\n{{/*0.75 {subtitle}}}" font 'Arial,16'
set border 3 lc rgb '#888888'; set tics nomirror tc rgb '#333333'
set grid ytics lc rgb '#e6e6e6'
set style data histograms; set style histogram clustered gap 1.5
set style fill solid border rgb 'white'; set boxwidth 0.9
set ylabel 'Time (s)'; set xlabel 'FEAScript version'; set yrange [0:{ymax:.3f}]
set key top right box lc rgb '#cccccc' opaque
plot '{case}.dat' u 3:xtic(1) t '{SOLVERS[0][1]}' lc rgb '{SOLVERS[0][2]}', \\
     '' u 4 t '{SOLVERS[1][1]}' lc rgb '{SOLVERS[1][2]}', \\
     '' u ($0-0.15):3:(sprintf('%.2f s',$3)) w labels offset 0,0.8 tc rgb '#333333' notitle, \\
     '' u ($0+0.15):4:(sprintf('%.2f s',$4)) w labels offset 0,0.8 tc rgb '#333333' notitle
"""
open(os.path.join(out, f"{case}.gnuplot"), "w").write(gp)
subprocess.run(["gnuplot", f"{case}.gnuplot"], cwd=out, check=True)
print(os.path.join(out, f"{case}.png"))
