<img src="https://feascript.github.io/FEAScript-website/assets/feascript-solver.png" width="80" alt="FEAScript solver logo">

# FEAScript-benchmark

This repository contains benchmarks for [FEAScript](https://feascript.com/), the finite element simulation library developed in JavaScript. Each benchmark runs FEAScript and established finite element software on the same problem and compares them on accuracy, run time and memory, against an exact solution where one exists. Results are kept for every machine and FEAScript version, so the comparison can be followed as FEAScript develops.

## Benchmarks

| Benchmark | Compared with | Problem |
|---|---|---|
| [heatConduction2DFin](heatConduction2DFin/) | Elmer, scikit-fem | 2D heat conduction in a fin with constant-temperature, symmetry and convection boundaries, on linear and quadratic quadrilateral meshes from 231 to 51,681 nodes |
| [heatConduction2DFinGmsh](heatConduction2DFinGmsh/) | Elmer, scikit-fem | The same fin on unstructured Gmsh meshes, with linear and quadratic triangles and distorted quadrilaterals |
| [creepingFlow2DLidDrivenCavity](creepingFlow2DLidDrivenCavity/) | Elmer, scikit-fem | Stokes (creeping) flow in the lid-driven unit cavity, with Taylor–Hood Q2–Q1 elements on meshes from 289 to 16,641 velocity nodes |

Each benchmark folder has a README with the problem, the setup, the results on each machine, FEAScript's speed-up by version and the steps to run it.

## Layout

Every benchmark folder has the same layout, shown here for the fin. Each code has a folder with its input and its results, and `reports/` holds the reports that bring them together:

```
heatConduction2DFin/
  README.md
  benchmark.py        runs all the codes and compares them
  make_report.py      writes the plots, results table and README of a run
  feascript/
    case.mjs, run_feascript.mjs
    results/<machine>/<FEAScript version>/
      node/<version>/
      chromium/<version>/
      firefox/<version>/
  elmer/
    case.sif.in
    meshes/           ElmerGrid meshes, not committed
    results/<machine>/<Elmer version>/
  scikit-fem/
    run_skfem.py
    results/<machine>/<scikit-fem version>/
  reports/<machine>/
    <FEAScript version>/   README, plots, results table, meta.json, results.json, run.log
    by-version/            FEAScript's speed-up by version
browser/              runs the cases of any benchmark in headless browsers
elmer_vtu.py          reads Elmer's binary VTU results
refresh_elmer.py      shared steps of REFRESH_ELMER=1
```

The results of each code are kept under its own version, since Elmer and scikit-fem do not change with the FEAScript version. Every run measures all the codes again, so that their times come from the same session: the `results.json` in a code's folder holds its latest numbers, and the one in `reports/` the numbers of all the codes in that run. Machines come first because times can only be compared on the same machine. Nodal results (`.csv`) are not committed.

To run every benchmark for a FEAScript version, build FEAScript-core and run `run_all.py` with the Python that has the benchmark packages:

```
FEASCRIPT_VERSION=0.4.0 ~/.venvs/feascript-benchmark/bin/python run_all.py
```

To write Elmer's nodal results again without measuring any times, run a benchmark with `REFRESH_ELMER=1`. It runs Elmer once on each mesh, then recomputes the accuracy columns of every report of the machine from the nodal results stored there, and keeps all the times:

```
cd heatConduction2DFin && REFRESH_ELMER=1 FEASCRIPT_VERSION=0.4.0 ~/.venvs/feascript-benchmark/bin/python benchmark.py
```

The timed Elmer runs write no results, so how Elmer writes them does not change any time.

## How the benchmarks are run

- **Same problem, same meshes:** the codes solve identical meshes, so their nodal results can be compared one to one
- **Full precision:** every code writes its nodal results in double precision. Elmer writes binary VTU files, since its ASCII VTU files have 8 significant digits
- **One core:** every timed process is pinned to one core, so neither code gains from multithreading
- **Fresh processes:** each timing is the median of several fresh processes
- **FEAScript as users load it:** the benchmarks load the built bundle `dist/feascript.esm.js` from a [FEAScript-core](https://github.com/FEAScript/FEAScript-core) checkout, by default the sibling folder `../FEAScript-core`
- **Recorded setup:** each run writes a `meta.json` with the FEAScript version and commit, the versions of the other software, the machine and its memory, the operating system, and the date
- **Machines:** the results so far were measured on an AMD Ryzen 5 9600X with 14.7 GB of usable RAM and on an Intel N100 with 7.5 GB, both on Linux Mint 22.3. Chromium and Firefox are the builds that it packages. The N100 is a low-power CPU whose speed varied by up to 20% between runs, so small differences on it mean little
- **Elmer build:** the results so far use a nightly build of Elmer from the [Elmer PPA](https://launchpad.net/~elmer-csc-ubuntu/+archive/ubuntu/elmer-csc-ppa), version 26.2, built from commit [`56b16bd49`](https://github.com/ElmerCSC/elmerfem/commit/56b16bd49564d5b16fdc57862ccda024043b0f39) of 2026-11-02, which is newer than the 26.2.1 release
- **One folder per machine and version:** results are kept by machine, and by the version of each code, so runs on different machines are never mixed. `make_history.py` plots FEAScript's speed-up by version for each benchmark and machine

## Browsers

The comparison of the codes runs in Node.js, which shares its V8 JavaScript engine with Chrome and other Chromium-based browsers. Every benchmark also runs FEAScript in Chromium and in Firefox, with its own SpiderMonkey engine, on some of its meshes:

- **Same code:** `feascript/case.mjs` builds the model for both Node.js and the page, from the built bundle `dist/feascript.esm.js`, and no JavaScript packages are needed
- **Fresh browsers:** every run starts a headless browser with a new, empty profile, and each time is the median of several runs. A case with a first solve over 20 s is timed once, with one repeated solve in the browsers and none in Node.js, and each report lists those cases
- **One core:** every process, including the helper processes of a browser, is pinned to one core
- **Main thread:** FEAScript runs on the main thread of the page, without a web worker
- **First and repeated solves:** the first solve in a fresh process includes JIT warm-up, as a user sees it when a page opens. The repeated solves come after it, in the same process
- **Timers:** browsers coarsen `performance.now()`, so the server sends the headers that isolate the page and give it their finest timers

Keep in mind when reading the results:

- **Engine versions:** Node.js and Chromium both use V8, in different versions, so differences between them come from the version and from the browser around it
- **Memory:** a browser has many processes, so its memory is not comparable with that of Node.js, and it is not measured
- **Start-up:** a browser with an empty profile takes much longer to start than Node.js, so end-to-end times are not what a user of an open browser waits for

## About the comparison

These benchmarks use [Elmer](https://www.elmerfem.org/), the open-source multiphysics finite element software developed by CSC – IT Center for Science, and [scikit-fem](https://github.com/kinnala/scikit-fem), an open-source finite element library for Python, as trusted references for checking and tracking FEAScript. They are not a ranking of these programs, which are built for different purposes:

- **Elmer** is a mature, parallel code for large multiphysics problems, typically in 3D. It runs on many cores and across many machines with MPI and OpenMP, and offers a wide range of solvers and preconditioners for large systems
- **scikit-fem** is a lightweight Python library for finite element assembly. It is written in Python, but its heavy work runs in the compiled code of NumPy and SciPy, so its times are not a comparison of Python with JavaScript
- **FEAScript** is a JavaScript library that runs in a single thread of a web browser or Node.js, for small and medium problems, teaching and web applications

To compare the codes on the same terms, the benchmarks run Elmer the way FEAScript runs: on one core, as a single MPI process, on small 2D problems. This is not how Elmer is meant to be used for large problems, and its parallel performance is not measured here. Keep in mind when reading the results:

- **Solver speed:** Elmer and scikit-fem assemble and solve these problems much faster than FEAScript on the larger meshes, even on one core
- **End-to-end time:** on small meshes FEAScript can finish first, because the Elmer build used here (an MPI-enabled build) spends a fixed time starting MPI at the beginning of every run, even with one process, from under a second to a few seconds depending on the machine. This is a fixed start-up cost, not solver speed, and it becomes negligible for the larger problems Elmer is designed for
- **Elmer settings:** the Elmer cases use standard settings and solvers (UMFPACK, MUMPS, BiCGStab with ILU0) chosen by the FEAScript team, not tuned by Elmer experts. Other settings may well make Elmer faster
- **scikit-fem settings:** scikit-fem uses its default direct solver (SuperLU from SciPy), with the settings chosen by the FEAScript team. Its other solvers are not measured
- **Timer resolution:** Elmer reports its solver time to 0.01 s, so its times on the smallest meshes are rounded
- **Comparing FEAScript versions:** each version is benchmarked at a different time, and the speed of a machine varies over time with its temperature and load, most on low-power CPUs. Small differences between versions can come from this variation; each benchmark folder gives the variation measured on its machines
- **Comparing machines:** the speed-up between FEAScript versions depends on the machine, because older versions were limited by memory access, which some machines do much faster than others

We are grateful to the Elmer and scikit-fem developers for making such capable software freely available.

## License

The benchmarks in this repository are released under the [MIT license](LICENSE), the same license as the [FEAScript core library](https://github.com/FEAScript/FEAScript-core).
