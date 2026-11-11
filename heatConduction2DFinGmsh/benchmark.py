#!/usr/bin/env python3
# ════════════════════════════════════════════════════════════════
#  FEAScript Benchmark
#  Finite Element Simulation in JavaScript
#  https://github.com/FEAScript/FEAScript-benchmark
#  MIT License © 2026 FEAScript
# ════════════════════════════════════════════════════════════════

"""FEAScript vs Elmer and scikit-fem benchmark: 2D fin on unstructured Gmsh meshes.

The fin of heatConduction2DFin (T=200 bottom & right, symmetry left, convection top, k=1) on triangular and
quadrilateral meshes made with Gmsh, read by all the codes. The meshes are not regular, so this tests what the
structured meshes do not: reading a mesh, distorted elements and the numbering they lead to.
"""
import json, os, platform, re, shutil, statistics, subprocess, sys, tempfile, time
from importlib.metadata import version
import numpy as np
from scipy.spatial import cKDTree

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
from browser import runner as browser_runner
from elmer_vtu import read_vtu as read_elmer_vtu
import refresh_elmer as refresh

HERE = os.path.dirname(os.path.abspath(__file__))
GMSH_MESHES = os.path.join(HERE, "gmsh", "meshes")  # generated from gmsh/fin.geo
ELMER_MESHES = os.path.join(HERE, "elmer", "meshes")  # the same meshes, converted by ElmerGrid
# FEAScript-core checkout to benchmark (default: the sibling folder next to this repository)
CORE = os.path.abspath(os.environ.get("FEASCRIPT_CORE") or os.path.join(HERE, "..", "..", "FEAScript-core"))
# Each FEAScript version gets its own results folders (override with FEASCRIPT_VERSION)
VERSION = os.environ.get("FEASCRIPT_VERSION") or json.load(open(os.path.join(CORE, "package.json")))["version"]
CPU = subprocess.run(["bash", "-c", "lscpu | sed -n 's/^Model name: *//p'"], capture_output=True, text=True).stdout.strip()
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

# (shape, order, target element size). Splitting triangles into quadrilaterals halves the size, so quads start coarser
CASES = [("tri", order, h) for order in ("linear", "quadratic") for h in (0.2, 0.1, 0.05, 0.025)] + \
        [("quad", order, h) for order in ("linear", "quadratic") for h in (0.4, 0.2, 0.1, 0.05)]
PIN = ["taskset", "-c", os.environ.get("CORE_ID", "0")]  # pin every timed process to one core
ENV = {**os.environ, "FEASCRIPT_CORE": CORE, "OMP_NUM_THREADS": "1", "OPENBLAS_NUM_THREADS": "1", "MKL_NUM_THREADS": "1"}
FEA_TIMEOUT = int(os.environ.get("FEA_TIMEOUT", 600))  # seconds per FEAScript process
REPS = int(os.environ.get("REPS", 5))
WARM = int(os.environ.get("WARM", 3))
ONLY = os.environ.get("ONLY")  # e.g. "tri-linear-h0.2" for quick tests
FEA_CFGS = {"FEAScript frontal": "frontal", "FEAScript sparse LU": "lusolve"}
SKFEM_CFGS = {"scikit-fem SuperLU": "matched", "scikit-fem fine integration": "fine"}
ELMER = "Elmer UMFPACK"


def analytic(x, y):
    """T(x,y) = 200 + sum A_n cos(l_n x) sinh(l_n y), l_n = (2n-1)pi/8 (accurate to < 1e-6 K)."""
    x = np.asarray(x, float); y = np.asarray(y, float)
    T = np.empty_like(x)
    for yv in np.unique(np.round(y, 9)):
        idx = np.where(np.abs(y - yv) < 1e-9)[0]
        nterms = 200000 if yv > 2 - 1e-9 else min(200000, int(60 / (2 - yv)) + 200)  # exp(-l(2-y)) decay
        acc = np.zeros(len(idx))
        for n0 in range(1, nterms + 1, 20000):
            n = np.arange(n0, min(n0 + 20000, nterms + 1))[None, :]
            lam = (2 * n - 1) * np.pi / 8
            b = -90.0 * (-1.0) ** (n + 1) / lam  # cosine coefficients of -180
            ratio = np.exp(lam * (yv - 2)) * (1 - np.exp(-2 * lam * yv)) / (lam * (1 + np.exp(-4 * lam)) + (1 - np.exp(-4 * lam)))
            acc += np.sum(b * ratio * np.cos(lam * x[idx, None]), axis=1)
        T[idx] = 200 + acc
    return T


def make_meshes(shape, order, h, name):
    """Generate the Gmsh mesh of a case and its ElmerGrid conversion."""
    msh = os.path.join(GMSH_MESHES, f"{name}.msh")
    elmer = os.path.join(ELMER_MESHES, name)
    os.makedirs(GMSH_MESHES, exist_ok=True)
    os.makedirs(ELMER_MESHES, exist_ok=True)
    if not os.path.exists(msh):
        subprocess.run(["gmsh", os.path.join(HERE, "gmsh", "fin.geo"), "-2", "-setnumber", "h", str(h), "-setnumber", "quads", str(int(shape == "quad")),
                        "-setnumber", "degree", "1" if order == "linear" else "2", "-format", "msh41", "-o", msh], check=True, capture_output=True)
    if not os.path.exists(os.path.join(elmer, "mesh.header")):
        # ElmerGrid writes next to its input, ignoring -out for Gmsh files, so it runs on a copy
        shutil.copy(msh, ELMER_MESHES)
        subprocess.run(["ElmerGrid", "14", "2", f"{name}.msh", "-autoclean"], check=True, capture_output=True, cwd=ELMER_MESHES)
        os.remove(os.path.join(ELMER_MESHES, f"{name}.msh"))
    restore_coordinates(msh, elmer)
    return msh, elmer


def restore_coordinates(msh, elmer):
    """Give the ElmerGrid mesh the exact node coordinates of the Gmsh mesh.

    ElmerGrid writes the coordinates with 12 significant digits, which moves the nodes of an unstructured mesh by
    up to about 1e-11 and changes Elmer's temperatures by up to about 1e-9. With the exact coordinates, Elmer
    solves on the same mesh as the other codes.
    """
    import meshio
    exact = meshio.read(msh).points[:, :2]
    path = os.path.join(elmer, "mesh.nodes")
    rows = [line.split() for line in open(path)]
    distance, nearest = cKDTree(exact).query(np.array([[float(r[2]), float(r[3])] for r in rows]))
    if distance.max() > 1e-9:
        raise RuntimeError(f"{path}: a node is {distance.max()} from the nearest Gmsh node")
    with open(path, "w") as f:
        f.writelines(f"{r[0]} {r[1]} {float(exact[k, 0])!r} {float(exact[k, 1])!r} {r[4]}\n" for r, k in zip(rows, nearest))


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


def run_elmer(mesh, write_output):
    sif = os.path.join(ELMER_OUT, "case.sif")
    with open(os.path.join(HERE, "elmer", "case.sif.in")) as f:
        s = f.read()
    s = (s.replace("@MESH@", os.path.relpath(mesh, ELMER_OUT)).replace("@OUTPUT@", "Always" if write_output else "Never").replace("@OUTNAME@", "case"))
    with open(sif, "w") as f:
        f.write(s)
    t0 = time.perf_counter()
    p = run_measured(PIN + ["ElmerSolver", "case.sif"], cwd=ELMER_OUT, env=ENV)
    wall = time.perf_counter() - t0
    log = p.stdout
    if "ALL DONE" not in log:
        raise RuntimeError(f"Elmer failed:\n{log[-3000:]}\n{p.stderr[-2000:]}")
    lin = [float(a) for a in re.findall(r"Linear system time \(CPU,REAL\) for temperature:\s+\S+\s+(\S+)", log)]
    slv = [float(a) for a in re.findall(r"Solver time \(CPU,REAL\) for heat equation:\s+\S+\s+(\S+)", log)]
    res = {"process": wall, "peakMemory": p.peakMemory, "wall": sum(slv), "linsolve": sum(lin)}
    if write_output:
        out = os.path.join(ELMER_OUT, os.path.basename(mesh))
        vtus = sorted(f for f in os.listdir(out) if f.startswith("case") and f.endswith(".vtu"))
        res["field"] = read_vtu(os.path.join(out, vtus[-1]))
        for v in vtus:
            os.remove(os.path.join(out, v))
    return res


def read_vtu(path):
    pts, data = read_elmer_vtu(path)
    return pts[:, 0], pts[:, 1], data["temperature"]


def run_timed(cmd, timeout=None):
    t0 = time.perf_counter()
    try:
        p = run_measured(cmd, env=ENV, timeout=timeout)
    except subprocess.TimeoutExpired:
        raise RuntimeError(f"timeout after {timeout} s")
    proc = time.perf_counter() - t0
    if p.returncode:
        raise RuntimeError(p.stderr[-3000:])
    r = json.loads(p.stdout.strip().splitlines()[-1])
    r["process"] = proc
    r["peakMemory"] = p.peakMemory
    return r


def run_fea(msh, method, csv=None, warm=0):
    r = run_timed(PIN + ["node", os.path.join(HERE, "feascript", "run_feascript.mjs"), msh, method, csv or "-", str(warm)], FEA_TIMEOUT)
    if any("did not converge" in e for e in r.get("errors", [])):
        raise RuntimeError(f"not converged: {r['errors'][0]}")
    r["wall"], r["linsolve"] = r["coldWall"], r["coldSystem"] or 0
    return r


def run_skfem(msh, integration, csv=None):
    return run_timed(PIN + [sys.executable, os.path.join(HERE, "scikit-fem", "run_skfem.py"), msh, integration, csv or "-"])


def read_csv(path):
    d = np.loadtxt(path, delimiter=",", skiprows=1)
    return d[:, 0], d[:, 1], d[:, 2]


def errors(field):
    x, y, T = field
    e = T - analytic(x, y)
    return {"maxErr": float(np.max(np.abs(e))), "rmsErr": float(np.sqrt(np.mean(e ** 2)))}


def max_difference(field, ref):
    """Largest difference at the same nodes. Unstructured coordinates are matched by distance, since the codes may number them differently."""
    distance, nearest = cKDTree(np.c_[ref[0], ref[1]]).query(np.c_[field[0], field[1]])
    if distance.max() > 1e-5:
        raise RuntimeError(f"the nodes of two codes differ, by up to {distance.max()}")
    return float(np.max(np.abs(field[2] - ref[2][nearest])))


def write_meta():
    """Record the versions and machine the results were produced with."""
    sh = lambda *c: subprocess.run(c, capture_output=True, text=True).stdout.strip()
    meta = {"feascriptVersion": VERSION,
            "feascriptPackageVersion": json.load(open(os.path.join(CORE, "package.json")))["version"],
            "feascriptCommit": os.environ.get("FEASCRIPT_COMMIT") or sh("git", "-C", CORE, "rev-parse", "--short", "HEAD"),
            "feascriptUncommittedChanges": False if os.environ.get("FEASCRIPT_COMMIT") else bool(sh("git", "-C", CORE, "status", "--porcelain", "src")),
            "feascriptReleaseDate": os.environ.get("FEASCRIPT_RELEASE_DATE"),
            "elmerVersion": ELMER_VERSION, "elmerCommit": ELMER_BUILD and ELMER_BUILD.group(4), "elmerBuildDate": ELMER_BUILD and "-".join(ELMER_BUILD.group(1, 2, 3)), "node": sh("node", "-v"),
            "skfemVersion": SKFEM_VERSION, "scipyVersion": version("scipy"), "numpyVersion": version("numpy"), "meshioVersion": version("meshio"), "python": platform.python_version(),
            "gmshVersion": sh("gmsh", "--version"), "machine": MACHINE, "cpu": CPU, "ramGB": RAM_GB, "distribution": platform.freedesktop_os_release().get("PRETTY_NAME"), "os": sh("uname", "-sr"), "date": time.strftime("%Y-%m-%d"),
            "feascriptEntry": "src/index.js" if os.environ.get("FEASCRIPT_ENTRY") == "src" else "dist/feascript.esm.js",
            "pinning": f"taskset -c {PIN[-1]}, OMP_NUM_THREADS=1, OPENBLAS_NUM_THREADS=1", "reps": REPS, "warm": WARM}
    with open(os.path.join(RUN, "meta.json"), "w") as f:
        json.dump(meta, f, indent=1)


def write_code_results(results):
    """Update the results of each code in its own folder, keeping the meshes that this run did not repeat."""
    for folder, prefix in ((FEA_OUT, "FEAScript"), (ELMER_OUT, "Elmer"), (SKFEM_OUT, "scikit-fem")):
        path = os.path.join(folder, "results.json")
        rows = json.load(open(path)) if os.path.exists(path) else []
        rows = {(r["case"], r["code"]): r for r in rows + [r for r in results if r["code"].startswith(prefix)]}
        with open(path, "w") as f:
            json.dump(list(rows.values()), f, indent=1)


def record(name, shape, order, h, code, runs, field, nodes):
    keep = [r for r in runs if r["process"] is not None]
    return {"case": name, "shape": shape, "order": order, "h": h, "nodes": nodes, "code": code,
            "solve": statistics.median(r["wall"] for r in runs), "linsolve": statistics.median(r["linsolve"] for r in runs),
            "process": statistics.median(r["process"] for r in keep), "peakMemoryMB": statistics.median(r["peakMemory"] for r in keep),
            "nruns": len(runs), **errors(field)}


def compare(name, fields, results):
    """Compare every code with FEAScript, at the same nodes."""
    if "FEAScript sparse LU" in fields:
        ref = fields["FEAScript sparse LU"]
        for r in results:
            if r["case"] == name and r["code"] in fields:
                r["maxDiffVsFEAScript"] = max_difference(fields[r["code"]], ref)


def refresh_elmer():
    """REFRESH_ELMER=1: write Elmer's nodal results again, and recompute the accuracy of every report of this machine."""
    for shape, order, h in CASES:
        name = f"{shape}-{order}-h{h}"
        if ONLY and name not in ONLY.split(","):
            continue
        _, elmer_mesh = make_meshes(shape, order, h, name)
        field = run_elmer(elmer_mesh, True)["field"]
        np.savetxt(os.path.join(ELMER_OUT, f"{name}.csv"), np.column_stack(field), delimiter=",", header="x,y,T", comments="", fmt="%.17g")
        print(f"== {name}: Elmer results written", flush=True)
    every = []
    for version, path, results, meta in refresh.reports(HERE, MACHINE):
        fea = os.path.join(HERE, "feascript", "results", MACHINE, version, "node", meta["node"].lstrip("v"))
        skfem = os.path.join(SKFEM_OUT, "..", meta["skfemVersion"])
        csvs = lambda name: {**{cfg: os.path.join(fea, f"{m}_{name}.csv") for cfg, m in FEA_CFGS.items()},
                             **{cfg: os.path.join(skfem, f"{i}_{name}.csv") for cfg, i in SKFEM_CFGS.items()},
                             ELMER: os.path.join(ELMER_OUT, "..", meta["elmerVersion"], f"{name}.csv")}
        for name in dict.fromkeys(r["case"] for r in results):
            rows = {r["code"]: r for r in results if r["case"] == name and "failed" not in r}
            fields = {cfg: read_csv(csvs(name)[cfg]) for cfg in rows}
            rows[ELMER].update(errors(fields[ELMER]))
            compare(name, fields, results)
        with open(path, "w") as f:
            json.dump(results, f, indent=1)
        print(f"== {version}: accuracy recomputed", flush=True)
        every += results
    refresh.sync_code_results(HERE, MACHINE, every, ["maxErr", "rmsErr", "maxDiffVsFEAScript"])


def run_codes():
    write_meta()
    out = os.path.join(RUN, "results.json")
    results = json.load(open(out)) if os.environ.get("RESUME") and os.path.exists(out) else []
    done = {r["case"] for r in results}
    for shape, order, h in CASES:
        name = f"{shape}-{order}-h{h}"
        if (ONLY and name not in ONLY.split(",")) or name in done:
            continue
        print(f"== {name}", flush=True)
        msh, elmer_mesh = make_meshes(shape, order, h, name)
        fields = {}
        for cfg, method in FEA_CFGS.items():
            csv = os.path.join(FEA_OUT, f"{method}_{name}.csv")
            try:
                first = run_fea(msh, method, csv)
            except RuntimeError as e:
                why = ("out of memory" if "heap out of memory" in str(e) else
                       f"timeout (> {FEA_TIMEOUT} s)" if "timeout after" in str(e) else "failed")
                results.append({"case": name, "shape": shape, "order": order, "h": h, "code": cfg, "failed": why})
                print(f"{cfg} {why}\n{str(e)[-400:]}", flush=True); continue
            # Slow cases (over 20 s) are timed once, without warm repeats
            if first["wall"] > 20:
                runs = [first]
            else:
                warm = run_fea(msh, method, warm=WARM)
                first["warm"] = warm["warm"]
                warm["process"] = None  # includes the warm repeats, so not an end-to-end time
                runs = [first, warm] + [run_fea(msh, method) for _ in range(REPS - 2)]
            fields[cfg] = read_csv(csv)
            rec = record(name, shape, order, h, cfg, runs, fields[cfg], first["nodes"])
            rec["warmWall"] = statistics.median(first["warm"]) if first.get("warm") else None
            results.append(rec)
        for cfg, integration in SKFEM_CFGS.items():
            csv = os.path.join(SKFEM_OUT, f"{integration}_{name}.csv")
            first = run_skfem(msh, integration, csv)
            fields[cfg] = read_csv(csv)
            results.append(record(name, shape, order, h, cfg, [run_skfem(msh, integration) for _ in range(REPS)], fields[cfg], first["nodes"]))
        first = run_elmer(elmer_mesh, True)
        fields[ELMER] = first["field"]
        np.savetxt(os.path.join(ELMER_OUT, f"{name}.csv"), np.column_stack(first["field"]), delimiter=",", header="x,y,T", comments="", fmt="%.17g")
        results.append(record(name, shape, order, h, ELMER, [run_elmer(elmer_mesh, False) for _ in range(REPS)], fields[ELMER], len(first["field"][0])))
        compare(name, fields, results)
        for r in results:
            if r["case"] == name:
                print(json.dumps(r), flush=True)
        with open(out, "w") as f:
            json.dump(results, f, indent=1)
    write_code_results(results)


def browser_cases():
    """The quadratic meshes in the browsers, against the nodal results of the Node.js run."""
    for shape, sizes, label in (("tri", (0.1, 0.05, 0.025), "triangles"), ("quad", (0.2, 0.1, 0.05), "quadrilaterals")):
        for h in sizes:
            name = f"{shape}-quadratic-h{h}"
            for code, method in (("FEAScript frontal", "frontal"), ("FEAScript sparse LU", "lusolve")):
                csv = os.path.join(FEA_OUT, f"{method}_{name}.csv")
                if (ONLY and name not in ONLY.split(",")) or not os.path.exists(csv):
                    continue
                T = np.loadtxt(csv, delimiter=",", skiprows=1)[:, 2]
                yield {"name": name, "code": code, "group": f"{code}, quadratic {label}", "nodes": len(T), "reference": T, "params": {"mesh": f"{name}.msh", "method": method}}


def main():
    if os.environ.get("REFRESH_ELMER"):
        return refresh_elmer()
    # NO_BROWSERS=1 runs only the codes, e.g. for a release older than the browser benchmarks, and ONLY_BROWSERS=1 only the browsers
    if not os.environ.get("ONLY_BROWSERS"):
        run_codes()
    if not os.environ.get("NO_BROWSERS"):
        browser_runner.run_cases(list(browser_cases()), os.path.join(HERE, "feascript", "case.mjs"), CORE, RUN, FEA_RESULTS, PIN, REPS, WARM, GMSH_MESHES)


if __name__ == "__main__":
    main()
