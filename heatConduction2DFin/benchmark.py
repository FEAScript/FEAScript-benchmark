#!/usr/bin/env python3
# ════════════════════════════════════════════════════════════════
#  FEAScript Benchmark
#  Finite Element Simulation in JavaScript
#  https://github.com/FEAScript/FEAScript-benchmark
#  MIT License © 2026 FEAScript
# ════════════════════════════════════════════════════════════════

"""FEAScript vs Elmer and scikit-fem benchmark: 2D fin (heat conduction), 4 x 2 domain.

BCs: T=200 bottom & right, symmetry left, convection (h=1, Tinf=20) top, k=1.
Runs the codes on identical structured meshes, compares nodal temperatures
against each other and against the analytical series solution, and times them.
"""
import json, os, platform, re, statistics, subprocess, sys, tempfile, time
from importlib.metadata import version
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
MESHES = os.path.join(HERE, "elmer", "meshes")  # shared ElmerGrid meshes
# FEAScript-core checkout to benchmark (default: the sibling folder next to this repository)
CORE = os.path.abspath(os.environ.get("FEASCRIPT_CORE") or os.path.join(HERE, "..", "..", "FEAScript-core"))
# Each FEAScript version gets its own results folders (override with FEASCRIPT_VERSION)
VERSION = os.environ.get("FEASCRIPT_VERSION") or json.load(open(os.path.join(CORE, "package.json")))["version"]
CPU = subprocess.run(["bash", "-c", "lscpu | sed -n 's/^Model name: *//p'"], capture_output=True, text=True).stdout.strip()
# Each machine and FEAScript version gets its own folders: the comparison of the codes in comparison/<machine>/<version>/
MACHINE = os.environ.get("FEASCRIPT_MACHINE") or re.sub(r"[^a-z0-9]+", "-", re.sub(r"\((r|tm)\)|\d+-core processor", "", CPU.lower())).strip("-")
RUN = os.path.join(HERE, "comparison", MACHINE, VERSION)
RAM_GB = round(int(re.search(r"MemTotal:\s+(\d+)", open("/proc/meminfo").read()).group(1)) / 1024 ** 2, 1)  # usable RAM
# Each code keeps its results in its own folder, under its own version: they do not change with the FEAScript version
ELMER_VERSION = (re.search(r"Version: (\d[\d.]*)", subprocess.run("ElmerSolver -v 2>&1 </dev/null | head -20", shell=True, capture_output=True, text=True).stdout) or [None, "unknown"])[1]
# A nightly package of the Elmer PPA names the commit and date it was built from, e.g. 9.0-0ppa0-202611021648~56b16bd49~ubuntu24.04.1
ELMER_BUILD = re.search(r"-(\d{4})(\d{2})(\d{2})\d{4}~([0-9a-f]+)~", subprocess.run(["dpkg-query", "-W", "-f", "${Version}", "elmerfem-csc"], capture_output=True, text=True).stdout)
SKFEM_VERSION = version("scikit-fem")
FEA_OUT = os.path.join(HERE, "feascript", "results", MACHINE, VERSION)
ELMER_OUT = os.path.join(HERE, "elmer", "results", MACHINE, ELMER_VERSION)
SKFEM_OUT = os.path.join(HERE, "scikit-fem", "results", MACHINE, SKFEM_VERSION)
for d in (RUN, FEA_OUT, ELMER_OUT, SKFEM_OUT):
    os.makedirs(d, exist_ok=True)

# (order, nx, ny)
CASES = [("linear", n, n // 2) for n in (20, 40, 80, 160, 320)] + [("linear", 77, 39)] + \
        [("quadratic", n, n // 2) for n in (10, 20, 40, 80, 160)]
PIN = ["taskset", "-c", os.environ.get("CORE_ID", "0")]  # pin every timed process to one core
ENV = {**os.environ, "FEASCRIPT_CORE": CORE, "OMP_NUM_THREADS": "1", "OPENBLAS_NUM_THREADS": "1", "MKL_NUM_THREADS": "1"}
FEA_TIMEOUT = int(os.environ.get("FEA_TIMEOUT", 600))  # seconds per FEAScript process
REPS = int(os.environ.get("REPS", 5))
WARM = int(os.environ.get("WARM", 3))
ONLY = os.environ.get("ONLY")  # e.g. "linear-20x10" for quick tests

LINSYS = {
    "bicgstab-ilu0": """  Linear System Solver = Iterative
  Linear System Iterative Method = BiCGStab
  Linear System Max Iterations = 5000
  Linear System Convergence Tolerance = 1.0e-10
  Linear System Preconditioning = ILU0
  Linear System Abort Not Converged = False""",
    "umfpack": """  Linear System Solver = Direct
  Linear System Direct Method = UMFPACK""",
    "mumps": """  Linear System Solver = Direct
  Linear System Direct Method = MUMPS""",
}
# name -> (linsys, steady-state iters, nonlinear iters)
ELMER_CFGS = {
    "Elmer BiCGStab+ILU0": ("bicgstab-ilu0", 1, 1),
    "Elmer UMFPACK": ("umfpack", 1, 1),
    "Elmer MUMPS": ("mumps", 1, 1),
}
FEA_CFGS = {"FEAScript frontal": "frontal", "FEAScript sparse LU": "lusolve", "FEAScript Jacobi": "jacobi"}
SKFEM = "scikit-fem SuperLU"


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


MESHGEN = {}


def make_mesh(order, nx, ny):
    d = os.path.join(MESHES, f"{order}_{nx}x{ny}")
    if os.path.exists(os.path.join(d, "mesh.header")):
        return d
    os.makedirs(os.path.dirname(d), exist_ok=True)
    grd = os.path.join(MESHES, f"{order}_{nx}x{ny}.grd")
    deg, inner = (1, "False") if order == "linear" else (2, "True")  # quadratic -> 9-node quads (409), like FEAScript
    with open(grd, "w") as f:
        f.write(f"""Version = 210903
Coordinate System = Cartesian 2D
Subcell Divisions in 2D = 1 1
Subcell Sizes 1 = 4
Subcell Sizes 2 = 2
Material Structure in 2D
  1
End
Materials Interval = 1 1
Boundary Definitions
  1 -3 1 1
  2 -4 1 1
  3 -1 1 1
  4 -2 1 1
End
Numbering = Horizontal
Element Degree = {deg}
Element Innernodes = {inner}
Element Divisions 1 = {nx}
Element Divisions 2 = {ny}
""")
    t0 = time.perf_counter()
    subprocess.run(PIN + ["ElmerGrid", "1", "2", grd, "-out", d], check=True, capture_output=True, env=ENV)
    MESHGEN[f"{order}-{nx}x{ny}"] = time.perf_counter() - t0
    return d


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


def run_elmer(mesh, cfg, write_output):
    linsys, ss, nl = ELMER_CFGS[cfg]
    tag = re.sub(r"\W+", "_", cfg)
    sif = os.path.join(ELMER_OUT, f"{tag}.sif")
    with open(os.path.join(HERE, "elmer", "case.sif.in")) as f:
        s = f.read()
    s = (s.replace("@MESH@", os.path.relpath(mesh, os.path.dirname(sif))).replace("@SSITER@", str(ss))
          .replace("@NLITER@", str(nl)).replace("@LINSYS@", LINSYS[linsys])
          .replace("@OUTPUT@", "Always" if write_output else "Never").replace("@OUTNAME@", tag))
    with open(sif, "w") as f:
        f.write(s)
    t0 = time.perf_counter()
    p = run_measured(PIN + ["ElmerSolver", os.path.basename(sif)], cwd=os.path.dirname(sif), env=ENV)
    wall = time.perf_counter() - t0
    log = p.stdout
    if "ALL DONE" not in log:
        raise RuntimeError(f"Elmer failed for {cfg}:\n{log[-3000:]}\n{p.stderr[-2000:]}")
    m = re.search(r"SOLVER TOTAL TIME\(CPU,REAL\):\s+(\S+)\s+(\S+)", log)
    lin = [float(a) for a in re.findall(r"Linear system time \(CPU,REAL\) for temperature:\s+\S+\s+(\S+)", log)]
    slv = [float(a) for a in re.findall(r"Solver time \(CPU,REAL\) for heat equation:\s+\S+\s+(\S+)", log)]
    res = {"wall": wall, "peakMemory": p.peakMemory, "solverReal": float(m.group(2)), "solve": sum(slv), "linsolve": sum(lin), "nsolves": len(lin)}
    if write_output:
        mesh_dir = os.path.join(os.path.dirname(sif), os.path.basename(mesh))  # Elmer writes next to the run, lowercased
        vtus = sorted(f for f in os.listdir(mesh_dir) if f.startswith(tag.lower()) and f.endswith(".vtu"))
        res["field"] = read_vtu(os.path.join(mesh_dir, vtus[-1]))
        for v in vtus:
            os.remove(os.path.join(mesh_dir, v))
    return res


def read_vtu(path):
    txt = open(path).read()
    def arr(name):
        m = re.search(rf'<DataArray[^>]*Name="{name}"[^>]*>(.*?)</DataArray>', txt, re.S)
        return np.array(m.group(1).split(), float)
    pts = re.search(r"<Points>\s*<DataArray[^>]*>(.*?)</DataArray>", txt, re.S).group(1).split()
    pts = np.array(pts, float).reshape(-1, 3)
    return pts[:, 0], pts[:, 1], arr("temperature")


def run_fea(order, nx, ny, method, csv=None, warm=0):
    cmd = PIN + ["node", os.path.join(HERE, "feascript", "run_feascript.mjs"), str(nx), str(ny), order, method, csv or "-", str(warm)]
    t0 = time.perf_counter()
    try:
        p = run_measured(cmd, env=ENV, timeout=FEA_TIMEOUT)
    except subprocess.TimeoutExpired:
        raise RuntimeError(f"timeout after {FEA_TIMEOUT} s")
    proc = time.perf_counter() - t0
    if p.returncode:
        raise RuntimeError(p.stderr[-3000:])
    r = json.loads(p.stdout.strip().splitlines()[-1])
    if any("did not converge" in e for e in r.get("errors", [])):
        raise RuntimeError(f"not converged: {r['errors'][0]}")
    r["process"] = proc
    r["peakMemory"] = p.peakMemory
    if csv:
        d = np.loadtxt(csv, delimiter=",", skiprows=1)
        r["field"] = (d[:, 0], d[:, 1], d[:, 2])
    return r


def run_skfem(order, nx, ny, csv=None):
    t0 = time.perf_counter()
    p = run_measured(PIN + [sys.executable, os.path.join(HERE, "scikit-fem", "run_skfem.py"), str(nx), str(ny), order, csv or "-"], env=ENV)
    proc = time.perf_counter() - t0
    if p.returncode:
        raise RuntimeError(p.stderr[-3000:])
    r = json.loads(p.stdout.strip().splitlines()[-1])
    r["process"] = proc
    r["peakMemory"] = p.peakMemory
    if csv:
        d = np.loadtxt(csv, delimiter=",", skiprows=1)
        r["field"] = (d[:, 0], d[:, 1], d[:, 2])
    return r


def keyed(x, y, T):
    return {(round(a, 7), round(b, 7)): t for a, b, t in zip(x, y, T)}


def errors(field):
    x, y, T = field
    Te = analytic(x, y)
    e = T - Te
    return {"maxErr": float(np.max(np.abs(e))), "rmsErr": float(np.sqrt(np.mean(e ** 2))),
            "Ttip": float(T[np.argmin(x ** 2 + (y - 2) ** 2)])}


def write_meta():
    """Record the versions and machine the results were produced with."""
    sh = lambda *c: subprocess.run(c, capture_output=True, text=True).stdout.strip()
    meta = {"feascriptVersion": VERSION,
            "feascriptPackageVersion": json.load(open(os.path.join(CORE, "package.json")))["version"],
            "feascriptCommit": os.environ.get("FEASCRIPT_COMMIT") or sh("git", "-C", CORE, "rev-parse", "--short", "HEAD"),
            "feascriptUncommittedChanges": False if os.environ.get("FEASCRIPT_COMMIT") else bool(sh("git", "-C", CORE, "status", "--porcelain", "src")),
            "feascriptReleaseDate": os.environ.get("FEASCRIPT_RELEASE_DATE"),
            "elmerVersion": ELMER_VERSION, "elmerCommit": ELMER_BUILD and ELMER_BUILD.group(4), "elmerBuildDate": ELMER_BUILD and "-".join(ELMER_BUILD.group(1, 2, 3)), "node": sh("node", "-v"),
            "skfemVersion": SKFEM_VERSION, "scipyVersion": version("scipy"), "numpyVersion": version("numpy"), "python": platform.python_version(),
            "machine": MACHINE, "cpu": CPU, "ramGB": RAM_GB, "os": sh("uname", "-sr"), "date": time.strftime("%Y-%m-%d"),
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


def main():
    write_meta()
    # RESUME=1 keeps the cases already in results.json and runs only the missing ones
    out = os.path.join(RUN, os.environ.get("OUTNAME", "results.json"))
    results = json.load(open(out)) if os.environ.get("RESUME") and os.path.exists(out) else []
    done = {r["case"] for r in results}
    for order, nx, ny in CASES:
        name = f"{order}-{nx}x{ny}"
        if ONLY and name not in ONLY.split(","):
            continue
        if name in done:
            print(f"== {name} (already done)", flush=True)
            continue
        mesh = make_mesh(order, nx, ny)
        print(f"== {name}", flush=True)
        fields = {}
        for cfg, method in FEA_CFGS.items():
            csv = os.path.join(FEA_OUT, f"{method}_{name}.csv")
            try:
                first = run_fea(order, nx, ny, method, csv)
            except RuntimeError as e:
                why = ("out of memory" if "heap out of memory" in str(e) else
                       f"timeout (> {FEA_TIMEOUT} s)" if "timeout after" in str(e) else
                       "not converged" if "not converged" in str(e) else "failed")
                results.append({"case": name, "order": order, "nx": nx, "ny": ny, "code": cfg, "failed": why})
                print(f"{cfg} {why}", flush=True); continue
            # Slow cases (over 20 s) are timed once, without warm repeats
            if first["coldWall"] > 20:
                runs = [first]
            else:
                warm = run_fea(order, nx, ny, method, warm=WARM)  # one more cold run, then the warm repeats in the same process
                first["warm"] = warm["warm"]
                warm["process"] = None  # includes the warm repeats, so not an end-to-end time
                runs = [first, warm] + [run_fea(order, nx, ny, method) for _ in range(REPS - 2)]
            fields[cfg] = first["field"]
            rec = {"case": name, "order": order, "nx": nx, "ny": ny, "nodes": first["nodes"], "code": cfg,
                   "wall": statistics.median(r["coldWall"] for r in runs),
                   "solve": statistics.median(r["coldWall"] for r in runs),
                   "process": statistics.median(r["process"] for r in runs if r["process"] is not None),
                   "peakMemoryMB": statistics.median(r["peakMemory"] for r in runs if r["process"] is not None),
                   "linsolve": statistics.median(r["coldSystem"] or 0 for r in runs),
                   "warmWall": statistics.median(first["warm"]) if first["warm"] else None,
                   "nruns": len(runs), **errors(first["field"])}
            results.append(rec); print(json.dumps(rec), flush=True)
        csv = os.path.join(SKFEM_OUT, f"{name}.csv")
        first = run_skfem(order, nx, ny, csv)
        runs = [run_skfem(order, nx, ny) for _ in range(REPS)]
        fields[SKFEM] = first["field"]
        rec = {"case": name, "order": order, "nx": nx, "ny": ny, "nodes": first["nodes"], "code": SKFEM,
               "wall": statistics.median(r["wall"] for r in runs),
               "solve": statistics.median(r["wall"] for r in runs),
               "process": statistics.median(r["process"] for r in runs),
               "peakMemoryMB": statistics.median(r["peakMemory"] for r in runs),
               "linsolve": statistics.median(r["linsolve"] for r in runs),
               "nruns": len(runs), **errors(first["field"])}
        results.append(rec); print(json.dumps(rec), flush=True)
        for cfg in ELMER_CFGS:
            first = run_elmer(mesh, cfg, True)
            runs = [run_elmer(mesh, cfg, False) for _ in range(REPS)]
            fields[cfg] = first["field"]
            tag = re.sub(r"\W+", "_", cfg)
            np.savetxt(os.path.join(ELMER_OUT, f"{tag}_{name}.csv"), np.column_stack(first["field"]), delimiter=",", header="x,y,T", comments="", fmt="%.17g")
            rec = {"case": name, "order": order, "nx": nx, "ny": ny, "nodes": len(first["field"][0]), "code": cfg,
                   "wall": statistics.median(r["solverReal"] for r in runs),
                   "process": statistics.median(r["wall"] for r in runs),
                   "peakMemoryMB": statistics.median(r["peakMemory"] for r in runs),
                   "solve": statistics.median(r["solve"] for r in runs),
                   "meshgen": MESHGEN.get(name),
                   "linsolve": statistics.median(r["linsolve"] for r in runs),
                   "nsolves": first["nsolves"], "nruns": len(runs), **errors(first["field"])}
            results.append(rec); print(json.dumps(rec), flush=True)
        # Code-to-code agreement on identical nodes
        ref = keyed(*fields["Elmer UMFPACK"])
        for cfg, f in fields.items():  # (failed runs have no field)
            k = keyed(*f)
            common = ref.keys() & k.keys()
            diff = max(abs(k[c] - ref[c]) for c in common)
            for r in results:
                if r["case"] == name and r["code"] == cfg:
                    r["maxDiffVsElmerUMFPACK"] = diff; r["matchedNodes"] = len(common)
        # Elmer writes 8 significant digits, so scikit-fem and FEAScript are also compared directly
        if "FEAScript sparse LU" in fields:
            A, B = keyed(*fields[SKFEM]), keyed(*fields["FEAScript sparse LU"])
            for r in results:
                if r["case"] == name and r["code"] == SKFEM:
                    r["maxDiffVsFEAScript"] = max(abs(A[c] - B[c]) for c in A.keys() & B.keys())
        print("   max |T - T_ElmerUMFPACK|: " + ", ".join(f"{r['code']}: {r['maxDiffVsElmerUMFPACK']:.2e}" for r in results if r["case"] == name and "maxDiffVsElmerUMFPACK" in r), flush=True)
        with open(os.path.join(RUN, os.environ.get("OUTNAME", "results.json")), "w") as f:
            json.dump(results, f, indent=1)
    with open(os.path.join(RUN, os.environ.get("OUTNAME", "results.json")), "w") as f:
        json.dump(results, f, indent=1)
    write_code_results(results)


if __name__ == "__main__":
    main()
