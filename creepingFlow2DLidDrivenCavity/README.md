<img src="https://feascript.github.io/FEAScript-website/assets/feascript-logo.png" width="80" alt="FEAScript Logo">

# FEAScript vs Elmer and scikit-fem benchmark: lid-driven cavity

This folder compares [FEAScript](https://feascript.com/) with the [Elmer](https://www.elmerfem.org/) finite element solver and the [scikit-fem](https://github.com/kinnala/scikit-fem) finite element library on Stokes (creeping) flow in the lid-driven cavity, a standard test of incompressible flow solvers and the problem of the [creeping flow example](https://github.com/FEAScript/FEAScript-core/tree/main/examples/creepingFlowScript) of FEAScript-core. The codes solve it with the same elements on identical meshes and are compared on the flow they compute and on run time. Each machine and FEAScript version gets its own set of results, so the comparison can be repeated as FEAScript develops.

## Contents

- [Results](#results)
- [The problem](#the-problem)
- [What is measured](#what-is-measured)
- [How to run the benchmark](#how-to-run-the-benchmark)
- [License](#license)

## Results

The report of each run is in `reports/<machine>/<FEAScript version>/`. The results of each code are in `<code>/results/<machine>/<its version>/`, and those of FEAScript also by runtime, in `feascript/results/<machine>/<FEAScript version>/<runtime>/<its version>/`:

| Machine | FEAScript version | Results |
|---|---|---|
| AMD Ryzen 5 9600X | 0.2.0 | [reports/amd-ryzen-5-9600x/0.2.0/](reports/amd-ryzen-5-9600x/0.2.0/) |
| AMD Ryzen 5 9600X | 0.3.1 | [reports/amd-ryzen-5-9600x/0.3.1/](reports/amd-ryzen-5-9600x/0.3.1/) |
| AMD Ryzen 5 9600X | 0.4.0-rc | [reports/amd-ryzen-5-9600x/0.4.0-rc/](reports/amd-ryzen-5-9600x/0.4.0-rc/) |

FEAScript's speed-up on the 32×32 mesh by version, with the assembly and solve time of each run, on the AMD Ryzen 5 9600X:

<img src="reports/amd-ryzen-5-9600x/by-version/32x32.png" width="600" alt="FEAScript speed-up by version on the AMD Ryzen 5 9600X">

Each report has a README with the plots of that run, a table of all the numbers (`results_table.md`) and the details of the run (`meta.json`): the FEAScript version and commit, the versions of the other software, the machine and the date. Runs on the AMD Ryzen 5 9600X with FEAScript 0.2.0 and 0.3.1 do not include scikit-fem, which was added with 0.4.0-rc.

> **About the comparison:** Elmer runs here on one core, as a single MPI process, on small 2D problems, so that both codes are compared on the same terms. Elmer is a parallel code built for much larger problems, and this setup does not show its parallel performance. Its end-to-end time includes a fixed MPI start-up in the build used here, about 0.5 s on the AMD Ryzen 5 9600X. See [About the comparison](../README.md#about-the-comparison).

## The problem

- **Domain:** unit square, viscosity μ = 1
- **Lid:** velocity (1, 0) on the top edge
- **Walls:** no-slip, velocity (0, 0), on the other three edges. The walls win at the two lid corners, so the lid moves only between them
- **Pressure:** fixed to 0 at (0, 0), since an enclosed flow determines the pressure only up to a constant
- **Elements:** Taylor–Hood Q2–Q1 quadrilaterals (quadratic velocity, linear pressure) in all the codes. FEAScript and scikit-fem use nodal Q2 elements; Elmer uses hierarchic Q2 velocity on a bilinear mesh (`Element = "p:2"`)

The problem has no exact solution, and the velocity is discontinuous at the two lid corners, where the moving lid meets the fixed walls.

## What is measured

The codes solve the problem on n × n meshes with n = 8, 16, 24, 32, 48 and 64, from 289 to 16,641 velocity nodes. On each mesh, the benchmark runs:

- **FEAScript:** the `lusolve` (math.js sparse LU) solver, the one that supports creeping flow, loaded from the built bundle `dist/feascript.esm.js` as npm and browser users load it, in Node
- **Elmer:** the `IncompressibleNSVec` solver with `Stokes Flow = True`, with the UMFPACK and MUMPS direct solvers
- **scikit-fem:** its default direct solver (SuperLU from SciPy), with the Stokes equations assembled in `scikit-fem/run_skfem.py`
- **FEAScript in browsers:** Chromium and Firefox, on the 8×8, 16×16, 32×32 and 64×64 meshes, with `lusolve`: see [Browsers](../README.md#browsers)

And compares:

- **Primary vortex strength:** the minimum of the stream function, ψ_min, which lies on the vertical centerline x = 0.5 because Stokes flow in the cavity is symmetric. It is computed the same way for all the codes, from the velocity at the mesh vertices on the centerline
- **Velocity:** the difference from Elmer at the mesh vertices, which all the codes share, over the whole cavity and away from the two lid corners
- **scikit-fem against FEAScript:** the difference in velocity at all their nodes, and in pressure at the mesh vertices
- **Centerline profile:** the velocity u along x = 0.5
- **Assembly and solve time:**
  - FEAScript: the time of `model.solve()`, which includes mesh generation
  - Elmer: the `Solver time` of the flow solver, at 0.01 s resolution
  - scikit-fem: the time of mesh generation, assembly and solve, like FEAScript's `model.solve()`, without writing the results
- **End-to-end time:** the wall time of the whole process, from start to exit, on the 16 × 16 mesh
- **Peak memory:** the largest resident memory of each process, as GNU time reports it. It is the memory of the whole process, so it includes Node and FEAScript, Python and its libraries, or Elmer, as well as the problem. Results from before this was measured have no memory

FEAScript and Elmer apply the lid velocity differently next to the corners. FEAScript sets the full lid velocity at every lid node, including the mid-edge node of the corner element. Elmer, with hierarchic elements, interpolates the boundary values linearly along each element edge, so along the top edge of the corner element the lid velocity rises from 0 at the corner. This is part of the comparison: the two codes differ near the two lid corners on every mesh, and agree away from them more closely as the mesh is refined. scikit-fem sets the lid velocity the same way as FEAScript, so these two are expected to agree at every node, lid corners included.

To keep the comparison fair, every timed process is pinned to one core (`taskset -c 0`, `OMP_NUM_THREADS=1`, `OPENBLAS_NUM_THREADS=1`), and each time is the median of several fresh processes. A run that runs out of memory or exceeds the time limit is recorded as such.

Notes on reading the times:

- **Browsers:** the codes are compared in Node, which uses the same V8 JavaScript engine as Chrome and other Chromium-based browsers. FEAScript also runs in Chromium and Firefox: see [Browsers](../README.md#browsers)
- **Comparing versions:** each version is benchmarked at a different time, and the speed of a machine varies over time. On the AMD Ryzen 5 9600X, repeated runs of the same build agree to within about 3%; smaller differences between versions in the history plot are within this variation
- **JIT warm-up:** each FEAScript time comes from a fresh process, so it includes JIT warm-up. Repeats inside the same process are in the `warmWall` column

## How to run the benchmark

The benchmark needs Node.js, Python 3 with NumPy, SciPy and scikit-fem, gnuplot, GNU time (`/usr/bin/time`, the `time` package), and ElmerSolver and ElmerGrid on the `PATH`. It benchmarks the [FEAScript-core](https://github.com/FEAScript/FEAScript-core) checkout next to this repository (`../../FEAScript-core` from this folder). Build it first with `npm run build`, since the benchmark loads `dist/feascript.esm.js`.

The Python packages can go in a virtual environment, and `meta.json` records their versions:

```
python3 -m venv ~/.venvs/feascript-benchmark
~/.venvs/feascript-benchmark/bin/pip install scikit-fem scipy numpy
```

Then run the benchmark with that Python:

```
~/.venvs/feascript-benchmark/bin/python benchmark.py   # writes <code>/results/ and reports/
python3 make_report.py <machine> <version>    # writes the plots, results_table.md and README.md
python3 ../make_history.py creepingFlow2DLidDrivenCavity  # updates the plots of FEAScript's speed-up by version in reports/<machine>/by-version/
```

The machine defaults to a name made from the CPU model, e.g. `amd-ryzen-5-9600x`, and the version to the `version` field of `FEAScript-core/package.json`. These environment variables change the run:

- **`FEASCRIPT_MACHINE`:** the name of the machine folder
- **`FEASCRIPT_CORE`:** the path of another FEAScript-core checkout, e.g. a released version
- **`FEASCRIPT_VERSION`:** the name of the version folder, e.g. `FEASCRIPT_VERSION=0.4.0`
- **`FEASCRIPT_COMMIT` and `FEASCRIPT_RELEASE_DATE`:** the commit and release date to record, when `FEASCRIPT_CORE` is not a git checkout
- **`FEASCRIPT_ENTRY=src`:** loads the source files instead of the built bundle
- **`CORE_ID`:** the CPU core to pin the runs to (default 0)
- **`REPS` and `WARM`:** the number of repeats and warm repeats
- **`FEA_TIMEOUT`:** the time limit of a FEAScript process, in seconds
- **`RESUME=1`:** keeps the meshes already in `results.json` and runs only the missing ones
- **`ONLY`:** runs only some meshes, e.g. `ONLY=8,16`
- **`NO_BROWSERS=1`:** runs only the codes, not the browsers, e.g. for a release older than the browser cases
- **`ONLY_BROWSERS=1`:** runs only the browsers, on the nodal results of the last Node.js run
- **`CHROMIUM_PATH`, `FIREFOX_PATH` and `BROWSER_TIMEOUT`:** other browsers to run, and the time limit of a browser run in seconds

After a run, add a row to [Results](#results) and run `make_history.py`, which picks up every folder in `reports/<machine>/`.

The files in this folder:

- **`benchmark.py`:** runs all the codes, compares them and writes the results
- **`make_report.py`:** draws the plots and writes the results table and README of a run
- **`feascript/run_feascript.mjs`:** runs one FEAScript case
- **`elmer/case.sif.in`:** the Elmer input template
- **`scikit-fem/run_skfem.py`:** runs one scikit-fem case
- **`elmer/meshes/`:** ElmerGrid meshes, shared by all runs and not committed
- **`feascript/case.mjs`:** the FEAScript model, shared by Node.js and the browsers
- **`feascript/results/<machine>/<FEAScript version>/<runtime>/<its version>/`:** the results of FEAScript in Node.js, Chromium and Firefox: `results.json`, and in Node.js centerline profiles, nodal results (not committed)
- **`elmer/results/<machine>/<its version>/` and `scikit-fem/results/<machine>/<its version>/`:** the latest results of Elmer and scikit-fem: `results.json`, centerline profiles, nodal results (not committed) and the Elmer `.sif` files
- **`reports/<machine>/<FEAScript version>/`:** the report of one run: README, plots, results table, `meta.json`, `results.json` and `browsers.json`
- **`reports/<machine>/by-version/`:** FEAScript's speed-up by version

## License

This benchmark is released under the [MIT license](../LICENSE). Note that the core library of FEAScript is distributed under the terms of the [MIT license](https://github.com/FEAScript/FEAScript-core/blob/main/LICENSE).
