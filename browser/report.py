# ════════════════════════════════════════════════════════════════
#  FEAScript Benchmark
#  Finite Element Simulation in JavaScript
#  https://github.com/FEAScript/FEAScript-benchmark
#  MIT License © 2026 FEAScript
# ════════════════════════════════════════════════════════════════

"""The browser part of a report: plots and a table from browsers.json, against the Node.js times of the same run."""
import json, os, re, subprocess

COLORS = {"node": "#1baf7a", "chromium": "#2a78d6", "firefox": "#eb6834"}
PT = {"node": 9, "chromium": 7, "firefox": 5}
NAMES = {"node": "Node.js", "chromium": "Chromium", "firefox": "Firefox"}
STYLE = """set terminal pngcairo size 900,620 font 'Arial,13'
set border 3 lc rgb '#888888'; set tics nomirror tc rgb '#333333'
set grid lc rgb '#e6e6e6' lw 1; set key top left box lc rgb '#cccccc' opaque
set logscale xy; set format y '10^{%L}'; set format x '10^{%L}'
"""


def no_repeat(results):
    """Return the markdown list of the FEAScript cases that Node.js timed without repeated solves, or nothing."""
    rows = [r for r in results if "failed" not in r and r["code"].startswith("FEAScript") and r.get("warmWall") is None]
    return ("\nRepeated solves that were not run, because the first solve took over 20 s and the case was timed once:\n" +
            "".join(f"\n- **{r['code']}, {r['case']}**" for r in rows) + "\n") if rows else ""


def section(run_dir, plots_dir, results, tag, title):
    """Return the markdown of the browser section of a run, or nothing for a run without browsers."""
    path = os.path.join(run_dir, "browsers.json")
    if not os.path.exists(path):
        return ""
    data = json.load(open(path))
    rows = [r for r in data["rows"] if "failed" not in r]
    node = {(r["case"], r["code"]): r for r in results if "failed" not in r}
    for r in list(rows):
        base = node[(r["case"], r["code"])]
        if not any(x["runtime"] == "node" and x["case"] == r["case"] and x["code"] == r["code"] for x in rows):
            rows.append({**r, "runtime": "node", "solve": base["solve"], "warmWall": base.get("warmWall"), "process": base["process"], "nodes": base["nodes"]})
    groups = list(dict.fromkeys(r["group"] for r in rows))
    images, table = "", "| Case | Nodes | Node.js | Chromium | Firefox |\n|---|---|---|---|---|\n"
    for group in groups:
        stem = "browsers_" + re.sub(r"\W+", "_", group).strip("_")
        chosen = [r for r in rows if r["group"] == group]
        for key, label, suffix in (("solve", "First solve", "first"), ("warmWall", "Repeated solves", "repeated")):
            lines = []
            for runtime in COLORS:
                pts = sorted((r["nodes"], r[key]) for r in chosen if r["runtime"] == runtime and r.get(key) is not None)
                if pts:
                    d = f"{stem}_{suffix}_{runtime}.dat"
                    with open(os.path.join(plots_dir, d), "w") as f:
                        f.write("".join(f"{a} {b}\n" for a, b in pts))
                    lines.append(f"'{d}' u 1:2 w lp lw 2 pt {PT[runtime]} ps 1.2 lc rgb '{COLORS[runtime]}' t '{NAMES[runtime]}'")
            if lines:
                name = f"{stem}_{suffix}"
                with open(os.path.join(plots_dir, f"{name}.gnuplot"), "w") as f:
                    f.write(STYLE + f"set output '{name}.png'\nset title '{label}: {group} ({tag})' font 'Arial,12'\nset xlabel 'Number of nodes'\nset ylabel 'Time (s)'\nplot " + ", \\\n     ".join(lines) + "\n")
                subprocess.run(["gnuplot", f"{name}.gnuplot"], cwd=plots_dir, check=True)
                images += f'<img src="plots/{name}.png" width="600" alt="{label}: {group}">\n'
        nodes = max(r["nodes"] for r in chosen)
        largest = {r["runtime"]: r for r in chosen if r["nodes"] == nodes}
        base = largest.get("node")
        cells = ["not measured" if rt not in largest else f"{largest[rt]['solve']:.2f} s" + ("" if rt == "node" else f" ({largest[rt]['solve'] / base['solve']:.1f}×)") for rt in COLORS]
        table += f"| {group} | {nodes:,} | " + " | ".join(cells) + " |\n"
    worst = max((r.get("maxDiffVsNode") or 0) for r in data["rows"])
    failed = [r for r in data["rows"] if "failed" in r]
    no_repeat = [r for r in data["rows"] if "failed" not in r and r.get("warmWall") is None]
    agree = "The browsers give the same solutions as Node.js, bit for bit." if worst == 0 else f"The solutions of the browsers match those of Node.js to within {worst:.1e}."
    versions = ", ".join(f"{NAMES[k]} {v}" for k, v in data["versions"].items())
    return f"""
## {title}

{versions}, each run in a fresh headless browser on one core, with FEAScript on the main thread of the page. The first solve in a fresh process on the largest mesh of each case, with the slowdown against Node.js:

{table}
{agree} Cases with a first solve over 20 s are timed once, with one repeated solve in the browsers and none in Node.js, instead of five times with three repeated solves. A case without a point on a plot was not measured, and each such case is listed in this report.
""" + ("\nRuns that could not be measured:\n" + "".join(f"\n- **{r['runtime']}, {r['case']}, {r['code']}:** {r['failed']}" for r in failed) + "\n" if failed else "") + \
        ("\nRepeated solves that could not be measured:\n" + "".join(f"\n- **{r['runtime']}, {r['case']}, {r['code']}:** {r.get('noRepeat', 'not run')}" for r in no_repeat) + "\n" if no_repeat else "") + "\n" + images
