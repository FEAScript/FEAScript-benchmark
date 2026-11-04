#!/usr/bin/env python3
# ════════════════════════════════════════════════════════════════
#  FEAScript Benchmark
#  Finite Element Simulation in JavaScript
#  https://github.com/FEAScript/FEAScript-benchmark
#  MIT License © 2026 FEAScript
# ════════════════════════════════════════════════════════════════

"""FEAScript vs Elmer benchmark: Stokes flow in the lid-driven unit cavity.

Lid velocity 1 on the top edge, no-slip on the other edges (the walls win at the two lid corners), viscosity 1,
pressure fixed to 0 at (0, 0). Both codes use Taylor-Hood Q2-Q1 elements on the same n x n meshes.
There is no exact solution, so the codes are compared with each other: velocity at the shared nodes, the
centerline velocity profile, and the strength of the primary vortex (the minimum of the stream function).
"""
import json, os, re, statistics, subprocess, sys, time
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "results")
# FEAScript-core checkout to benchmark (default: the sibling folder next to this repository)
CORE = os.path.abspath(os.environ.get("FEASCRIPT_CORE") or os.path.join(HERE, "..", "..", "FEAScript-core"))
VERSION = os.environ.get("FEASCRIPT_VERSION") or json.load(open(os.path.join(CORE, "package.json")))["version"]


def sh(*cmd):
    return subprocess.run(cmd, capture_output=True, text=True).stdout.strip()


CPU = sh("bash", "-c", "lscpu | sed -n 's/^Model name: *//p'")
# Each machine and FEAScript version gets its own results folder: results/<machine>/<version>/
MACHINE = os.environ.get("FEASCRIPT_MACHINE") or re.sub(r"[^a-z0-9]+", "-", re.sub(r"\((r|tm)\)", "", CPU.lower())).strip("-")
RUN = os.path.join(OUT, MACHINE, VERSION)
os.makedirs(RUN, exist_ok=True)

PIN = ["taskset", "-c", os.environ.get("CORE_ID", "0")]  # pin every timed process to one core
ENV = {**os.environ, "FEASCRIPT_CORE": CORE, "OMP_NUM_THREADS": "1", "OPENBLAS_NUM_THREADS": "1", "MKL_NUM_THREADS": "1"}
FEA_TIMEOUT = int(os.environ.get("FEA_TIMEOUT", 1800))  # seconds per FEAScript process
REPS = int(os.environ.get("REPS", 5))
WARM = int(os.environ.get("WARM", 3))
ONLY = os.environ.get("ONLY")  # e.g. "16" for a quick test
SIZES = [8, 16, 24, 32, 48, 64]
CORNER_RADIUS = 0.2  # "away from the lid corners": farther than this from (0, 1) and (1, 1)

LINSYS = {
    "Elmer UMFPACK": """  Linear System Solver = Direct
  Linear System Direct Method = UMFPACK""",
    "Elmer MUMPS": """  Linear System Solver = Direct
  Linear System Direct Method = MUMPS""",
}


def write_meta():
    """Record the versions and machine the results were produced with."""
    elmer = re.search(r"Version: (\S+)", sh("bash", "-c", "ElmerSolver -v 2>&1 </dev/null | head -20"))
    meta = {"feascriptVersion": VERSION,
            "feascriptPackageVersion": json.load(open(os.path.join(CORE, "package.json")))["version"],
            "feascriptCommit": os.environ.get("FEASCRIPT_COMMIT") or sh("git", "-C", CORE, "rev-parse", "--short", "HEAD"),
            "feascriptUncommittedChanges": False if os.environ.get("FEASCRIPT_COMMIT") else bool(sh("git", "-C", CORE, "status", "--porcelain", "src")),
            "feascriptReleaseDate": os.environ.get("FEASCRIPT_RELEASE_DATE"),
            "feascriptEntry": "src/index.js" if os.environ.get("FEASCRIPT_ENTRY") == "src" else "dist/feascript.esm.js",
            "elmerVersion": elmer.group(1) if elmer else None, "node": sh("node", "-v"),
            "machine": MACHINE, "cpu": CPU, "os": sh("uname", "-sr"), "date": time.strftime("%Y-%m-%d"),
            "pinning": f"taskset -c {PIN[-1]}, OMP_NUM_THREADS=1, OPENBLAS_NUM_THREADS=1", "reps": REPS, "warm": WARM}
    with open(os.path.join(RUN, "meta.json"), "w") as f:
        json.dump(meta, f, indent=1)


def make_mesh(n):
    d = os.path.join(OUT, "meshes", f"cavity_{n}x{n}")
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
    txt = open(path).read()
    def arr(name, ncomp):
        m = re.search(rf'<DataArray[^>]*Name="{name}"[^>]*>(.*?)</DataArray>', txt, re.S)
        return np.array(m.group(1).split(), float).reshape(-1, ncomp)
    pts = np.array(re.search(r"<Points>\s*<DataArray[^>]*>(.*?)</DataArray>", txt, re.S).group(1).split(), float).reshape(-1, 3)
    vel = arr("velocity", 3)
    return pts[:, 0], pts[:, 1], vel[:, 0], vel[:, 1], arr("pressure", 1)[:, 0]


def run_elmer(n, cfg, write_output):
    mesh, corners = make_mesh(n)
    tag = re.sub(r"\W+", "_", cfg)
    work = os.path.join(RUN, "work")
    os.makedirs(work, exist_ok=True)
    s = open(os.path.join(HERE, "case.sif.in")).read()
    s = (s.replace("@MESH@", os.path.relpath(mesh, work)).replace("@CORNERS@", " ".join(map(str, corners)))
          .replace("@LINSYS@", LINSYS[cfg]).replace("@OUTPUT@", "Always" if write_output else "Never")
          .replace("@OUTNAME@", tag))
    sif = os.path.join(work, f"{tag}.sif")
    open(sif, "w").write(s)
    t0 = time.perf_counter()
    p = subprocess.run(PIN + ["ElmerSolver", os.path.basename(sif)], cwd=work, capture_output=True, text=True, env=ENV)
    wall = time.perf_counter() - t0
    log = p.stdout
    if "ALL DONE" not in log:
        raise RuntimeError(f"Elmer failed for {cfg}:\n{log[-3000:]}\n{p.stderr[-2000:]}")
    m = re.search(r"SOLVER TOTAL TIME\(CPU,REAL\):\s+(\S+)\s+(\S+)", log)
    lin = [float(a) for a in re.findall(r"Linear system time \(CPU,REAL\) for flow solution:\s+\S+\s+(\S+)", log)]
    slv = [float(a) for a in re.findall(r"Solver time \(CPU,REAL\) for navier-stokes:\s+\S+\s+(\S+)", log)]
    res = {"wall": wall, "solverReal": float(m.group(2)), "solve": sum(slv), "linsolve": sum(lin)}
    if write_output:
        out_dir = os.path.join(work, os.path.basename(mesh))
        vtus = sorted(f for f in os.listdir(out_dir) if f.startswith(tag.lower()) and f.endswith(".vtu"))
        res["field"] = read_vtu(os.path.join(out_dir, vtus[-1]))
        for v in vtus:
            os.remove(os.path.join(out_dir, v))
    return res


def run_fea(n, csv=None, warm=0):
    cmd = PIN + ["node", os.path.join(HERE, "run_feascript.mjs"), str(n), csv or "-", str(warm)]
    t0 = time.perf_counter()
    try:
        p = subprocess.run(cmd, capture_output=True, text=True, env=ENV, timeout=FEA_TIMEOUT)
    except subprocess.TimeoutExpired:
        raise RuntimeError(f"timeout after {FEA_TIMEOUT} s")
    proc = time.perf_counter() - t0
    if p.returncode:
        raise RuntimeError(p.stderr[-3000:])
    r = json.loads(p.stdout.strip().splitlines()[-1])
    r["process"] = proc
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


def main():
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
        csv = os.path.join(RUN, "work", f"fea_{name}.csv")
        os.makedirs(os.path.dirname(csv), exist_ok=True)
        try:
            # The first run writes the results; slow cases (over 20 s) are timed once, without warm repeats
            first = run_fea(n, csv)
            if first["coldWall"] > 20:
                runs = [first]
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
                            "warmWall": statistics.median(first["warm"]) if first["warm"] else None,
                            "nruns": len(runs)})
        except RuntimeError as e:
            why = ("out of memory" if "heap out of memory" in str(e) else
                   f"timeout (> {FEA_TIMEOUT} s)" if "timeout after" in str(e) else "failed")
            results.append({"case": name, "n": n, "code": "FEAScript sparse LU", "failed": why})
            print(f"FEAScript sparse LU {why}", flush=True)
        for cfg in LINSYS:
            first = run_elmer(n, cfg, True)
            runs = [run_elmer(n, cfg, False) for _ in range(REPS)]
            fields[cfg] = first["field"]
            results.append({"case": name, "n": n, "nodes": (2 * n + 1) ** 2, "code": cfg,
                            "solve": statistics.median(r["solve"] for r in runs),
                            "linsolve": statistics.median(r["linsolve"] for r in runs),
                            "process": statistics.median(r["wall"] for r in runs), "nruns": len(runs)})
        # Compare every code with Elmer UMFPACK at the shared (vertex) nodes, and on the centerline
        ref = keyed(fields["Elmer UMFPACK"])
        for cfg, field in fields.items():
            D = keyed(field)
            common = list(ref.keys() & D.keys())
            far = [k for k in common if min((k[0] - c) ** 2 + (k[1] - 1) ** 2 for c in (0, 1)) > CORNER_RADIUS ** 2]
            ys, u, psi, ypsi = centerline(D, n)
            tag = re.sub(r"\W+", "_", cfg)
            np.savetxt(os.path.join(RUN, "work", f"centerline_{tag}_{name}.dat"), np.c_[ys, u],
                       header="y u(0.5, y)")
            for r in results:
                if r["case"] == name and r["code"] == cfg:
                    r.update({"psiMin": psi, "psiMinY": ypsi,
                              "maxDiffVelocity": max(max(abs(D[k][0] - ref[k][0]), abs(D[k][1] - ref[k][1])) for k in common),
                              "maxDiffVelocityAwayFromCorners": max(max(abs(D[k][0] - ref[k][0]), abs(D[k][1] - ref[k][1])) for k in far),
                              "matchedNodes": len(common)})
        for r in results:
            if r["case"] == name:
                print(json.dumps({k: v for k, v in r.items()}), flush=True)
        json.dump(results, open(out, "w"), indent=1)


if __name__ == "__main__":
    main()
