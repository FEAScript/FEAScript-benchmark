#!/usr/bin/env python3
# ════════════════════════════════════════════════════════════════
#  FEAScript Benchmark
#  Finite Element Simulation in JavaScript
#  https://github.com/FEAScript/FEAScript-benchmark
#  MIT License © 2026 FEAScript
# ════════════════════════════════════════════════════════════════

"""Plot FEAScript's speed-up by version (assembly and solve time), for each benchmark and machine.

Reads every <benchmark>/results/<machine>/<version>/ folder and writes <benchmark>/history/<machine>/<case>.png.

Usage: python3 make_history.py [benchmark ...] [--case CASE]
"""
import argparse, json, os, re, subprocess

HERE = os.path.dirname(os.path.abspath(__file__))
COLORS = {"FEAScript frontal": "#eb6834", "FEAScript sparse LU": "#2a78d6"}
# Changes that explain a jump in a solver's time between two versions (shown on the plot with the measured speed-up)
CHANGES = {
    ("0.2.0", "0.3.1", "FEAScript sparse LU"): "Sparse matrix assembly (0.3.0, #99)",
    ("0.2.0", "0.3.0", "FEAScript sparse LU"): "Sparse matrix assembly (#99)",
    ("0.3.1", "0.4.0-rc", "FEAScript frontal"): "Frontal solver fix (0.4.0, #121)",
    ("0.3.1", "0.4.0", "FEAScript frontal"): "Frontal solver fix (#121)",
}
# The mesh shown by default for each benchmark, and how to describe it
BENCHMARKS = {
    "heatConduction2DFin": ("linear-160x80", "2D fin heat conduction, 160×80 linear quads"),
    "creepingFlow2DLidDrivenCavity": ("32x32", "Lid-driven cavity (Stokes flow), 32×32 Q2–Q1 mesh"),
}


def version_key(version):
    """Order versions numerically, with a pre-release (e.g. 0.4.0-rc) before its release."""
    nums = [int(n) for n in re.findall(r"\d+", version.split("-")[0])]
    return (nums, "-" not in version, version)


def plot(bench, machine, case, label):
    root = os.path.join(HERE, bench, "results", machine)
    rows, metas = [], []
    for version in os.listdir(root):
        run = os.path.join(root, version)
        if not os.path.isfile(os.path.join(run, "results.json")):
            continue
        recs = {r["code"]: r for r in json.load(open(os.path.join(run, "results.json"))) if r["case"] == case}
        if recs:
            rows.append((version_key(version), version, recs))
            metas.append(json.load(open(os.path.join(run, "meta.json"))))
    if not rows:
        return None
    rows.sort()
    codes = [c for c in COLORS if any(c in recs for _, _, recs in rows)]
    nodes = next(r["nodes"] for _, _, recs in rows for r in recs.values() if "nodes" in r)

    # Speed-up of each solver relative to the first version in which it could be measured
    versions = [v for _, v, _ in rows]
    value = lambda i, c: rows[i][2].get(c, {}).get("solve")
    base = {c: next((value(i, c) for i in range(len(rows)) if value(i, c)), None) for c in codes}
    base_version = {c: next((versions[i] for i in range(len(rows)) if value(i, c)), None) for c in codes}
    speedup = lambda i, c: base[c] / value(i, c) if value(i, c) else None

    out = os.path.join(HERE, bench, "history", machine)
    os.makedirs(out, exist_ok=True)
    with open(os.path.join(out, f"{case}.dat"), "w") as f:
        f.write("# version " + " ".join(f"{c.split()[-2]}_{c.split()[-1]}_speedup {c.split()[-2]}_{c.split()[-1]}_seconds" for c in codes)
                + "  (assembly + solve; NaN = not measured)\n")
        for i, version in enumerate(versions):
            f.write(version + " " + " ".join(f"{speedup(i, c):.4g} {value(i, c):.3f}" if value(i, c) else "NaN NaN" for c in codes) + "\n")

    ymax = max(speedup(i, c) for i in range(len(rows)) for c in codes if value(i, c)) * 1.45
    width = 0.7 / len(codes)
    offset = {c: (j - (len(codes) - 1) / 2) * width for j, c in enumerate(codes)}

    # Notes on the changes behind a jump, above the bar of the version that brought them
    notes = ""
    for (v0, v1, c), text in CHANGES.items():
        if v0 in versions and v1 in versions and c in codes:
            i0, i1 = versions.index(v0), versions.index(v1)
            t0, t1 = value(i0, c), value(i1, c)
            if t0 and t1 and t0 / t1 > 1.5:
                notes += (f"set label \"{text}\" at {i1 + offset[c]:.2f},{speedup(i1, c):.4g} center offset 0,4.3 "
                          f"tc rgb '{COLORS[c]}' font ',11'\n")
    # Runs that could not be measured get a note in place of the bar (e.g. "out of memory")
    for i, (_, _, recs) in enumerate(rows):
        for c in codes:
            why = recs.get(c, {}).get("failed")
            if why:
                reason = "out of memory" if "memory" in why else why.split(" (")[0]
                notes += f"set label '{reason}' at {i + offset[c]:.2f},{ymax * 0.02:.4g} rotate by 90 left tc rgb '{COLORS[c]}' font ',11'\n"
    baselines = "; ".join(f"{c.replace('FEAScript ', '')} vs {base_version[c]}" for c in codes)
    subtitle = (f"{label} ({nodes:,} nodes) · {', '.join(sorted({m['cpu'] for m in metas}))}, 1 core, "
                f"Node {', '.join(sorted({m['node'] for m in metas}))}")
    series = ", \\\n     ".join(
        [f"'{case}.dat' u ($0{offset[c]:+.3f}):{2 * j + 2}{':xtic(1)' if j == 0 else ''} w boxes fs solid noborder lc rgb '{COLORS[c]}' t '{c.replace('FEAScript ', '')}'" for j, c in enumerate(codes)]
        + [f"'' u ($0{offset[c]:+.3f}):{2 * j + 2}:(sprintf(${2 * j + 2} < 10 ? '{{/:Bold %.1f×}}\\n%.2f s' : '{{/:Bold %.0f×}}\\n%.2f s',${2 * j + 2},${2 * j + 3})) w labels offset 0,1.6 tc rgb '#333333' font ',11' notitle" for j, c in enumerate(codes)])
    gp = f"""set terminal pngcairo size 1000,640 font 'Arial,13'
set output '{case}.png'
set title "FEAScript speed-up by version\\n{{/*0.75 {subtitle}}}" font 'Arial,16'
set border 3 lc rgb '#888888'; set tics nomirror tc rgb '#333333'
set grid ytics lc rgb '#e6e6e6'
set boxwidth {width * 0.9:.3f}
set xrange [-0.6:{len(rows) - 0.4}]; set yrange [0:{ymax:.4g}]; set xtics scale 0
set ylabel 'Speed-up (assembly + solve), × the first version'; set xlabel 'FEAScript version'
set key top left box lc rgb '#cccccc' opaque
set bmargin 5
set label "Each version was run at a different time; differences of up to about 20% can come from variation in the machine's speed" at screen 0.5,0.03 center tc rgb '#777777' font ',11'
set label "Relative to the first version each solver ran in: {baselines}" at graph 0.99,0.97 right tc rgb '#777777' font ',11'
set arrow from graph 0, first 1 to graph 1, first 1 nohead dt 2 lc rgb '#999999'
{notes}plot {series}
"""
    open(os.path.join(out, f"{case}.gnuplot"), "w").write(gp)
    subprocess.run(["gnuplot", f"{case}.gnuplot"], cwd=out, check=True)
    return os.path.join(out, f"{case}.png")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("benchmarks", nargs="*", default=list(BENCHMARKS))
    ap.add_argument("--case", help="mesh case to plot, e.g. linear-80x40 (default: the benchmark's usual one)")
    args = ap.parse_args()
    for bench in args.benchmarks:
        case, label = BENCHMARKS[bench]
        if args.case:
            case = args.case
        results = os.path.join(HERE, bench, "results")
        for machine in sorted(os.listdir(results)):
            if machine == "meshes" or not os.path.isdir(os.path.join(results, machine)):
                continue
            png = plot(bench, machine, case, label if case == BENCHMARKS[bench][0] else case)
            if png:
                print(png)


if __name__ == "__main__":
    main()
