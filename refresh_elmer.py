# ════════════════════════════════════════════════════════════════
#  FEAScript Benchmark
#  Finite Element Simulation in JavaScript
#  https://github.com/FEAScript/FEAScript-benchmark
#  MIT License © 2026 FEAScript
# ════════════════════════════════════════════════════════════════

"""Shared steps of REFRESH_ELMER=1, which writes Elmer's nodal results again and recomputes the accuracy columns.

Only the first Elmer run of each mesh writes its results: the timed runs write none, so a change to how Elmer
writes its results leaves every time valid. The refresh therefore keeps all the times of the existing reports,
and recomputes their accuracy columns from the nodal results (.csv) that the codes stored locally.
"""
import glob, json, os


def reports(here, machine):
    """Yield (version, path, rows, meta) for each report of this machine."""
    for path in sorted(glob.glob(os.path.join(here, "reports", machine, "*", "results.json"))):
        folder = os.path.dirname(path)
        yield os.path.basename(folder), path, json.load(open(path)), json.load(open(os.path.join(folder, "meta.json")))


def sync_code_results(here, machine, report_rows, keys):
    """Copy the recomputed accuracy columns into the results.json of each code's own folder.

    A row of a code folder is the same run as a row of a report when the case, code and times are the same.
    """
    runs = {(r["case"], r["code"], r.get("solve"), r.get("process")): r for r in report_rows if "solve" in r}
    folders = glob.glob(os.path.join(here, "feascript", "results", machine, "*", "node", "*")) + \
        glob.glob(os.path.join(here, "elmer", "results", machine, "*")) + glob.glob(os.path.join(here, "scikit-fem", "results", machine, "*"))
    for folder in folders:
        path = os.path.join(folder, "results.json")
        if not os.path.exists(path):
            continue
        rows = json.load(open(path))
        for r in rows:
            run = runs.get((r["case"], r["code"], r.get("solve"), r.get("process")))
            if run:
                r.update({k: run[k] for k in keys if k in run})
        with open(path, "w") as f:
            json.dump(rows, f, indent=1)
