#!/usr/bin/env python3
# ════════════════════════════════════════════════════════════════
#  FEAScript Benchmark
#  Finite Element Simulation in JavaScript
#  https://github.com/FEAScript/FEAScript-benchmark
#  MIT License © 2026 FEAScript
# ════════════════════════════════════════════════════════════════

"""FEAScript vs Elmer and scikit-fem benchmark: Stokes flow in the lid-driven unit cavity.

Lid velocity 1 on the top edge, no-slip on the other edges (the walls win at the two lid corners), viscosity 1,
pressure fixed to 0 at (0, 0). All the codes use Taylor-Hood Q2-Q1 elements on the same n x n meshes.
There is no exact solution, so the codes are compared with each other: velocity at the shared nodes, the
centerline velocity profile, and the strength of the primary vortex (the minimum of the stream function).
"""
import json, os, platform, re, statistics, subprocess, sys, tempfile, time
from importlib.metadata import version
import numpy as np

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
from browser import runner as browser_runner
from elmer_vtu import read_vtu as read_elmer_vtu
import refresh_elmer as refresh

HERE = os.path.dirname(os.path.abspath(__file__))
MESHES = os.path.join(HERE, "elmer", "meshes")  # shared ElmerGrid meshes
# FEAScript-core checkout to benchmark (default: the sibling folder next to this repository)
CORE = os.path.abspath(os.environ.get("FEASCRIPT_CORE") or os.path.join(HERE, "..", "..", "FEAScript-core"))
VERSION = os.environ.get("FEASCRIPT_VERSION") or json.load(open(os.path.join(CORE, "package.json")))["version"]


def sh(*cmd):
    return subprocess.run(cmd, capture_output=True, text=True).stdout.strip()


CPU = sh("bash", "-c", "lscpu | sed -n 's/^Model name: *//p'")
# Each machine and FEAScript version gets its own folders: the report of the run in reports/<machine>/<version>/
MACHINE = os.environ.get("FEASCRIPT_MACHINE") or re.sub(r"[^a-z0-9]+", "-", re.sub(r"\((r|tm)\)|\d+-core processor", "", CPU.lower())).strip("-")
RUN = os.path.join(HERE, "reports", MACHINE, VERSION)
RAM_GB = round(int(re.search(r"MemTotal:\s+(\d+)", open("/proc/meminfo").read()).group(1)) / 1024 ** 2, 1)  # usable RAM
# Each code keeps its results in its own folder, under its own version: they do not change with the FEAScript version
ELMER_VERSION = (re.search(r"Version: (\d[\d.]*)", subprocess.run("ElmerSolver -v 2>&1 </dev/null | head -20", shell=True, capture_output=True, text=True).stdout) or [None, "unknown"])[1]
# A nightly package of the Elmer PPA names the commit and date it was built from, e.g. 9.0-0ppa0-202611021648~56b16bd49~ubuntu24.04.1
ELMER_BUILD = re.search(r"-(\d{4})(\d{2})(\d{2})\d{4}~([0-9a-f]+)~", subprocess.run(["dpkg-query", "-W", "-f", "${Version}", "elmerfem-csc"], capture_output=True, text=True).stdout)
SKFEM_VERSION = version("scikit-fem")
NODE_VERSION = subprocess.run(["node", "-v"], capture_output=True, text=True).stdout.strip().lstrip("v")
FEA_RESULTS = os.path.join(HERE, "feascript", "results", MACHINE, VERSION)  # By runtime: node/, chromium/ and firefox/
FEA_OUT = os.path.join(FEA_RESULTS, "node", NODE_VERSION)
ELMER_OUT = os.path.join(HERE, "elmer", "results", MACHINE, ELMER_VERSION)
SKFEM_OUT = os.path.join(HERE, "scikit-fem", "results", MACHINE, SKFEM_VERSION)
for d in (RUN, FEA_OUT, ELMER_OUT, SKFEM_OUT):
    os.makedirs(d, exist_ok=True)

PIN = ["taskset", "-c", os.environ.get("CORE_ID", "0")]  # pin every timed process to one core
ENV = {**os.environ, "FEASCRIPT_CORE": CORE, "OMP_NUM_THREADS": "1", "OPENBLAS_NUM_THREADS": "1", "MKL_NUM_THREADS": "1"}
FEA_TIMEOUT = int(os.environ.get("FEA_TIMEOUT", 1800))  # seconds per FEAScript process
REPS = int(os.environ.get("REPS", 5))
WARM = int(os.environ.get("WARM", 3))
ONLY = os.environ.get("ONLY")  # e.g. "16" for a quick test
SIZES = [8, 16, 24, 32, 48, 64]
SKFEM = "scikit-fem SuperLU"
CORNER_RADIUS = 0.2  # "away from the lid corners": farther than this from (0, 1) and (1, 1)

LINSYS = {
    "Elmer UMFPACK": """  Linear System Solver = Direct
  Linear System Direct Method = UMFPACK""",
    "Elmer MUMPS": """  Linear System Solver = Direct
  Linear System Direct Method = MUMPS""",
}


def write_meta():
    """Record the versions and machine the results were produced with."""
    meta = {"feascriptVersion": VERSION,
            "feascriptPackageVersion": json.load(open(os.path.join(CORE, "package.json")))["version"],
            "feascriptCommit": os.environ.get("FEASCRIPT_COMMIT") or sh("git", "-C", CORE, "rev-parse", "--short", "HEAD"),
            "feascriptUncommittedChanges": False if os.environ.get("FEASCRIPT_COMMIT") else bool(sh("git", "-C", CORE, "status", "--porcelain", "src")),
            "feascriptReleaseDate": os.environ.get("FEASCRIPT_RELEASE_DATE"),
            "feascriptEntry": "src/index.js" if os.environ.get("FEASCRIPT_ENTRY") == "src" else "dist/feascript.esm.js",
            "elmerVersion": ELMER_VERSION, "elmerCommit": ELMER_BUILD and ELMER_BUILD.group(4), "elmerBuildDate": ELMER_BUILD and "-".join(ELMER_BUILD.group(1, 2, 3)), "node": sh("node", "-v"),
            "skfemVersion": SKFEM_VERSION, "scipyVersion": version("scipy"), "numpyVersion": version("numpy"), "python": platform.python_version(),
            "machine": MACHINE, "cpu": CPU, "ramGB": RAM_GB, "distribution": platform.freedesktop_os_release().get("PRETTY_NAME"), "os": sh("uname", "-sr"), "date": time.strftime("%Y-%m-%d"),
            "pinning": f"taskset -c {PIN[-1]}, OMP_NUM_THREADS=1, OPENBLAS_NUM_THREADS=1", "reps": REPS, "warm": WARM}
    with open(os.path.join(RUN, "meta.json"), "w") as f:
        json.dump(meta, f, indent=1)


def make_mesh(n):
    d = os.path.join(MESHES, f"cavity_{n}x{n}")
    if not os.path.exists(os.path.join(d, "mesh.header")):
        os.makedirs(os.path.dirname(d), exist_ok=True)
        grd = d + ".grd"
        with open(grd, "w") as f:
            f.write(f"""Version = 210903
Coordinate System = Cartesian 2D
Subcell Divisions in 2D = 1 1
Subcell Sizes 1 = 1
Subcell Sizes 2 = 1
Material Structure in 2D
  1
End
Materials Interval = 1 1
Boundary Definitions
  1 -1 1 1
  2 -2 1 1
  3 -3 1 1
  4 -4 1 1
End
Numbering = Horizontal
Element Degree = 1
Element Innernodes = False
Element Divisions 1 = {n}
Element Divisions 2 = {n}
""")
        subprocess.run(PIN + ["ElmerGrid", "1", "2", grd, "-out", d], check=True, capture_output=True, env=ENV)
    # Node numbers of the two lid corners, (0, 1) and (1, 1)
    nodes = np.loadtxt(os.path.join(d, "mesh.nodes"))
    corners = [int(nodes[np.argmin((nodes[:, 2] - x) ** 2 + (nodes[:, 3] - 1) ** 2), 0]) for x in (0, 1)]
    return d, corners


def read_vtu(path):
    pts, data = read_elmer_vtu(path)
    return pts[:, 0], pts[:, 1], data["velocity"][:, 0], data["velocity"][:, 1], data["pressure"]


def run_measured(cmd, timeout=None, **kwargs):
    """subprocess.run with captured text output that also returns the peak memory of the process, in MB.

    The command runs under GNU time, which reports its maximum resident set size. Measuring it from Python
    instead (wait4) would count the memory of this Python process, which a child inherits until it starts
    the command. Raises subprocess.TimeoutExpired after `timeout` seconds, once the whole process group
    has been stopped.
    """
    with tempfile.NamedTemporaryFile("r") as usage:
        p = subprocess.Popen(["/usr/bin/time", "-f", "%M", "-o", usage.name] + cmd, stdout=subprocess.PIPE,
                             stderr=subprocess.PIPE, text=True, start_new_session=True, **kwargs)
        try:
            out, err = p.communicate(timeout=timeout)
        except subprocess.TimeoutExpired:
            os.killpg(p.pid, 9)
            p.communicate()
            raise
        result = subprocess.CompletedProcess(cmd, p.returncode, out, err)
        kb = usage.read().strip().splitlines()
    result.peakMemory = int(kb[-1]) / 1024 if kb and kb[-1].isdigit() else None  # GNU time reports kB
    return result


def run_elmer(n, cfg, write_output):
    mesh, corners = make_mesh(n)
    tag = re.sub(r"\W+", "_", cfg)
    s = open(os.path.join(HERE, "elmer", "case.sif.in")).read()
    s = (s.replace("@MESH@", os.path.relpath(mesh, ELMER_OUT)).replace("@CORNERS@", " ".join(map(str, corners)))
          .replace("@LINSYS@", LINSYS[cfg]).replace("@OUTPUT@", "Always" if write_output else "Never")
          .replace("@OUTNAME@", tag))
    sif = os.path.join(ELMER_OUT, f"{tag}.sif")
    open(sif, "w").write(s)
    t0 = time.perf_counter()
    p = run_measured(PIN + ["ElmerSolver", os.path.basename(sif)], cwd=ELMER_OUT, env=ENV)
    wall = time.perf_counter() - t0
    log = p.stdout
    if "ALL DONE" not in log:
        raise RuntimeError(f"Elmer failed for {cfg}:\n{log[-3000:]}\n{p.stderr[-2000:]}")
    m = re.search(r"SOLVER TOTAL TIME\(CPU,REAL\):\s+(\S+)\s+(\S+)", log)
    lin = [float(a) for a in re.findall(r"Linear system time \(CPU,REAL\) for flow solution:\s+\S+\s+(\S+)", log)]
    slv = [float(a) for a in re.findall(r"Solver time \(CPU,REAL\) for navier-stokes:\s+\S+\s+(\S+)", log)]
    res = {"wall": wall, "peakMemory": p.peakMemory, "solverReal": float(m.group(2)), "solve": sum(slv), "linsolve": sum(lin)}
    if write_output:
        out_dir = os.path.join(ELMER_OUT, os.path.basename(mesh))
        vtus = sorted(f for f in os.listdir(out_dir) if f.startswith(tag.lower()) and f.endswith(".vtu"))
        res["field"] = read_vtu(os.path.join(out_dir, vtus[-1]))
        for v in vtus:
            os.remove(os.path.join(out_dir, v))
    return res


def run_fea(n, csv=None, warm=0):
    cmd = PIN + ["node", os.path.join(HERE, "feascript", "run_feascript.mjs"), str(n), csv or "-", str(warm)]
    t0 = time.perf_counter()
    try:
        p = run_measured(cmd, env=ENV, timeout=FEA_TIMEOUT)
    except subprocess.TimeoutExpired:
        raise RuntimeError(f"timeout after {FEA_TIMEOUT} s")
    proc = time.perf_counter() - t0
    if p.returncode:
        raise RuntimeError(p.stderr[-3000:])
    r = json.loads(p.stdout.strip().splitlines()[-1])
    r["process"] = proc
    r["peakMemory"] = p.peakMemory
    if csv:
        d = np.loadtxt(csv, delimiter=",", skiprows=1)
        r["field"] = tuple(d[:, i] for i in range(5))
    return r


def run_skfem(n, csv=None):
    t0 = time.perf_counter()
    p = run_measured(PIN + [sys.executable, os.path.join(HERE, "scikit-fem", "run_skfem.py"), str(n), csv or "-"], env=ENV)
    proc = time.perf_counter() - t0
    if p.returncode:
        raise RuntimeError(p.stderr[-3000:])
    r = json.loads(p.stdout.strip().splitlines()[-1])
    r["process"] = proc
    r["peakMemory"] = p.peakMemory
    if csv:
        d = np.loadtxt(csv, delimiter=",", skiprows=1)
        r["field"] = tuple(d[:, i] for i in range(5))
    return r


def keyed(field):
    x, y, u, v, p = field
    return {(round(a, 7), round(b, 7)): (c, d, e) for a, b, c, d, e in zip(x, y, u, v, p)}


def centerline(D, n):
    """u along x = 0.5 at the vertex nodes, and the stream function minimum psi_min = min_y int_0^y u dy."""
    # Vertex nodes lie at y = k/n; the mid-edge nodes of the Q2 elements lie halfway between (coordinates are rounded)
    ys = np.array(sorted(y for (x, y) in D if abs(x - 0.5) < 1e-6 and abs(y * n - round(y * n)) < 0.25))
    u = np.array([D[(0.5, round(y, 7))][0] for y in ys])
    psi = np.concatenate([[0], np.cumsum(0.5 * (u[1:] + u[:-1]) * np.diff(ys))])
    i = int(np.argmin(psi))
    if 0 < i < len(psi) - 1:  # refine with a parabola through the minimum and its neighbours
        a, b, c = np.polyfit(ys[i - 1:i + 2], psi[i - 1:i + 2], 2)
        y0 = -b / (2 * a)
        return ys, u, float(a * y0 ** 2 + b * y0 + c), float(y0)
    return ys, u, float(psi[i]), float(ys[i])


def write_code_results(results):
    """Update the results of each code in its own folder, keeping the meshes that this run did not repeat."""
    for folder, prefix in ((FEA_OUT, "FEAScript"), (ELMER_OUT, "Elmer"), (SKFEM_OUT, "scikit-fem")):
        path = os.path.join(folder, "results.json")
        rows = json.load(open(path)) if os.path.exists(path) else []
        rows = {(r["case"], r["code"]): r for r in rows + [r for r in results if r["code"].startswith(prefix)]}
        with open(path, "w") as f:
            json.dump(list(rows.values()), f, indent=1)


def compare(name, n, fields, results, fea_out, skfem_out, elmer_out):
    """Compare every code with Elmer UMFPACK at the shared (vertex) nodes and on the centerline, and scikit-fem with FEAScript."""
    ref = keyed(fields["Elmer UMFPACK"])
    for cfg, field in fields.items():
        D = keyed(field)
        common = list(ref.keys() & D.keys())
        far = [k for k in common if min((k[0] - c) ** 2 + (k[1] - 1) ** 2 for c in (0, 1)) > CORNER_RADIUS ** 2]
        ys, u, psi, ypsi = centerline(D, n)
        tag = re.sub(r"\W+", "_", cfg)
        folder = fea_out if cfg.startswith("FEAScript") else skfem_out if cfg == SKFEM else elmer_out
        np.savetxt(os.path.join(folder, f"centerline_{tag}_{name}.dat"), np.c_[ys, u],
                   header="y u(0.5, y)")
        for r in results:
            if r["case"] == name and r["code"] == cfg:
                r.update({"psiMin": psi, "psiMinY": ypsi,
                          "maxDiffVelocity": max(max(abs(D[k][0] - ref[k][0]), abs(D[k][1] - ref[k][1])) for k in common),
                          "maxDiffVelocityAwayFromCorners": max(max(abs(D[k][0] - ref[k][0]), abs(D[k][1] - ref[k][1])) for k in far),
                          "matchedNodes": len(common)})
    # scikit-fem sets the lid velocity like FEAScript, so the two are compared directly, at all their nodes
    if "FEAScript sparse LU" in fields and SKFEM in fields:
        A, B = keyed(fields[SKFEM]), keyed(fields["FEAScript sparse LU"])
        common = A.keys() & B.keys()
        for r in results:
            if r["case"] == name and r["code"] == SKFEM:
                r["maxDiffVelocityVsFEAScript"] = max(max(abs(A[k][0] - B[k][0]), abs(A[k][1] - B[k][1])) for k in common)
                r["matchedNodesVsFEAScript"] = len(common)
                r["maxDiffPressureVsFEAScript"] = float(np.nanmax([abs(A[k][2] - B[k][2]) for k in common]))  # at the mesh vertices


def refresh_elmer():
    """REFRESH_ELMER=1: write Elmer's nodal results again, and recompute the accuracy of every report of this machine."""
    for n in SIZES:
        name = f"{n}x{n}"
        if ONLY and str(n) not in ONLY.split(","):
            continue
        for cfg in LINSYS:
            tag = re.sub(r"\W+", "_", cfg)
            field = run_elmer(n, cfg, True)["field"]
            np.savetxt(os.path.join(ELMER_OUT, f"{tag}_{name}.csv"), np.column_stack(field), delimiter=",", header="x,y,u,v,p", comments="", fmt="%.17g")
        print(f"== {name}: Elmer results written", flush=True)
    every = []
    for version, path, results, meta in refresh.reports(HERE, MACHINE):
        fea = os.path.join(HERE, "feascript", "results", MACHINE, version, "node", meta["node"].lstrip("v"))
        skfem = os.path.join(SKFEM_OUT, "..", meta["skfemVersion"]) if meta.get("skfemVersion") else None
        elmer = os.path.join(ELMER_OUT, "..", meta["elmerVersion"])
        for name in dict.fromkeys(r["case"] for r in results):
            rows = {r["code"]: r for r in results if r["case"] == name and "failed" not in r}
            csvs = {"FEAScript sparse LU": os.path.join(fea, f"{name}.csv"), SKFEM: skfem and os.path.join(skfem, f"{name}.csv"),
                    **{cfg: os.path.join(elmer, re.sub(r"\W+", "_", cfg) + f"_{name}.csv") for cfg in LINSYS}}
            fields = {}
            for cfg in rows:
                d = np.loadtxt(csvs[cfg], delimiter=",", skiprows=1)
                fields[cfg] = tuple(d[:, i] for i in range(5))
            compare(name, rows["Elmer UMFPACK"]["n"], fields, results, fea, skfem, elmer)
        with open(path, "w") as f:
            json.dump(results, f, indent=1)
        print(f"== {version}: accuracy recomputed", flush=True)
        every += results
    refresh.sync_code_results(HERE, MACHINE, every, ["psiMin", "psiMinY", "maxDiffVelocity", "maxDiffVelocityAwayFromCorners", "matchedNodes",
                                                     "maxDiffVelocityVsFEAScript", "matchedNodesVsFEAScript", "maxDiffPressureVsFEAScript"])


def run_codes():
    write_meta()
    out = os.path.join(RUN, "results.json")
    results = json.load(open(out)) if os.environ.get("RESUME") and os.path.exists(out) else []
    done = {r["case"] for r in results}
    for n in SIZES:
        name = f"{n}x{n}"
        if (ONLY and str(n) not in ONLY.split(",")) or name in done:
            continue
        print(f"== {name}", flush=True)
        fields = {}
        csv = os.path.join(FEA_OUT, f"{name}.csv")
        try:
            # The first run writes the results. Slow cases (over 20 s) are timed once, with a single repeated solve in a run of its own, as in the browsers
            first = run_fea(n, csv)
            if first["coldWall"] > 20:
                runs = [first]
                first["warm"] = run_fea(n, warm=1)["warm"]
            else:
                warm = run_fea(n, warm=WARM)  # one more cold run, followed by the warm repeats in the same process
                first["warm"] = warm["warm"]
                warm["process"] = None  # includes the warm repeats, so not an end-to-end time
                runs = [first, warm] + [run_fea(n) for _ in range(REPS - 2)]
            fields["FEAScript sparse LU"] = first["field"]
            nodes = len(first["field"][0])
            results.append({"case": name, "n": n, "nodes": nodes, "code": "FEAScript sparse LU",
                            "solve": statistics.median(r["coldWall"] for r in runs),
                            "linsolve": statistics.median(r["coldSystem"] or 0 for r in runs),
                            "process": statistics.median(r["process"] for r in runs if r["process"] is not None),
                            "peakMemoryMB": statistics.median(r["peakMemory"] for r in runs if r["process"] is not None),
                            "warmWall": statistics.median(first["warm"]) if first["warm"] else None,
                            "nruns": len(runs)})
        except RuntimeError as e:
            why = ("out of memory" if "heap out of memory" in str(e) else
                   f"timeout (> {FEA_TIMEOUT} s)" if "timeout after" in str(e) else "failed")
            results.append({"case": name, "n": n, "code": "FEAScript sparse LU", "failed": why})
            print(f"FEAScript sparse LU {why}", flush=True)
        first = run_skfem(n, os.path.join(SKFEM_OUT, f"{name}.csv"))
        runs = [run_skfem(n) for _ in range(REPS)]
        fields[SKFEM] = first["field"]
        results.append({"case": name, "n": n, "nodes": first["nodes"], "code": SKFEM,
                        "solve": statistics.median(r["wall"] for r in runs),
                        "linsolve": statistics.median(r["linsolve"] for r in runs),
                        "process": statistics.median(r["process"] for r in runs),
                        "peakMemoryMB": statistics.median(r["peakMemory"] for r in runs), "nruns": len(runs)})
        for cfg in LINSYS:
            first = run_elmer(n, cfg, True)
            runs = [run_elmer(n, cfg, False) for _ in range(REPS)]
            fields[cfg] = first["field"]
            tag = re.sub(r"\W+", "_", cfg)
            np.savetxt(os.path.join(ELMER_OUT, f"{tag}_{name}.csv"), np.column_stack(first["field"]), delimiter=",", header="x,y,u,v,p", comments="", fmt="%.17g")
            results.append({"case": name, "n": n, "nodes": (2 * n + 1) ** 2, "code": cfg,
                            "solve": statistics.median(r["solve"] for r in runs),
                            "linsolve": statistics.median(r["linsolve"] for r in runs),
                            "process": statistics.median(r["wall"] for r in runs), "peakMemoryMB": statistics.median(r["peakMemory"] for r in runs), "nruns": len(runs)})
        compare(name, n, fields, results, FEA_OUT, SKFEM_OUT, ELMER_OUT)
        for r in results:
            if r["case"] == name:
                print(json.dumps({k: v for k, v in r.items()}), flush=True)
        json.dump(results, open(out, "w"), indent=1)
    write_code_results(results)


def browser_cases():
    """Some of the meshes in the browsers, against the nodal results of the Node.js run."""
    for n in (8, 16, 32, 64):
        name = f"{n}x{n}"
        csv = os.path.join(FEA_OUT, f"{name}.csv")
        if (ONLY and str(n) not in ONLY.split(",")) or not os.path.exists(csv):
            continue
        u = np.loadtxt(csv, delimiter=",", skiprows=1)[:, 2]
        yield {"name": name, "code": "FEAScript sparse LU", "group": "Lid-driven cavity, sparse LU", "nodes": len(u), "reference": u, "params": {"n": n}}


def main():
    if os.environ.get("REFRESH_ELMER"):
        return refresh_elmer()
    # NO_BROWSERS=1 runs only the codes, e.g. for a release older than the browser benchmarks, and ONLY_BROWSERS=1 only the browsers
    if not os.environ.get("ONLY_BROWSERS"):
        run_codes()
    if not os.environ.get("NO_BROWSERS"):
        browser_runner.run_cases(list(browser_cases()), os.path.join(HERE, "feascript", "case.mjs"), CORE, RUN, FEA_RESULTS, PIN, REPS, WARM, None)


if __name__ == "__main__":
    main()
