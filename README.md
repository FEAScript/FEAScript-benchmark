<img src="https://feascript.github.io/FEAScript-website/assets/feascript-logo.png" width="80" alt="FEAScript Logo">

# FEAScript-benchmark

This repository contains benchmarks for [FEAScript](https://feascript.com/), the finite element simulation library developed in JavaScript. Each benchmark runs FEAScript and established finite element software on the same problem and compares them on accuracy, run time and memory, against an exact solution where one exists. Results are kept for every machine and FEAScript version, so the comparison can be followed as FEAScript develops.

## Benchmarks

| Benchmark | Compared with | Problem |
|---|---|---|
| [heatConduction2DFin](heatConduction2DFin/) | [Elmer](https://www.elmerfem.org/), [scikit-fem](https://github.com/kinnala/scikit-fem) | 2D heat conduction in a fin with constant-temperature, symmetry and convection boundaries, on linear and quadratic quadrilateral meshes from 231 to 51,681 nodes |
| [creepingFlow2DLidDrivenCavity](creepingFlow2DLidDrivenCavity/) | [Elmer](https://www.elmerfem.org/), [scikit-fem](https://github.com/kinnala/scikit-fem) | Stokes (creeping) flow in the lid-driven unit cavity, with Taylor–Hood Q2–Q1 elements on meshes from 289 to 16,641 velocity nodes |

Each benchmark folder has a README with the problem, the setup, the results on each machine, FEAScript's speed-up by version and the steps to run it.

## Layout

Every benchmark folder has the same layout. Each code has its own folder with its input and its results, and `comparison/` holds what brings the codes together:

```
heatConduction2DFin/
  README.md
  benchmark.py        runs all the codes and compares them
  make_report.py      writes the plots, results table and README of a run
  feascript/
    run_feascript.mjs
    results/<machine>/<FEAScript version>/
  elmer/
    case.sif.in
    meshes/           ElmerGrid meshes, not committed
    results/<machine>/<Elmer version>/
  scikit-fem/
    run_skfem.py
    results/<machine>/<scikit-fem version>/
  comparison/<machine>/<FEAScript version>/
    README.md, results.json, results_table.md, meta.json, run.log
    plots/
  history/<machine>/  FEAScript's speed-up by version
```

The results of each code are kept under its own version, since Elmer and scikit-fem do not change with the FEAScript version. Every run measures all the codes again, so that their times come from the same session: the `results.json` in a code's folder holds its latest numbers, and the one in `comparison/` the numbers of all the codes in that run. Nodal results (`.csv`) are not committed.

## How the benchmarks are run

- **Same problem, same meshes:** the codes solve identical meshes, so their nodal results can be compared one to one
- **One core:** every timed process is pinned to one core, so neither code gains from multithreading
- **Fresh processes:** each timing is the median of several fresh processes
- **FEAScript as users load it:** the benchmarks load the built bundle `dist/feascript.esm.js` from a [FEAScript-core](https://github.com/FEAScript/FEAScript-core) checkout, by default the sibling folder `../FEAScript-core`
- **Recorded setup:** each run writes a `meta.json` with the FEAScript version and commit, the versions of the other software, the machine and its memory, and the date
- **Elmer build:** the results so far use a nightly build of Elmer from the [Elmer PPA](https://launchpad.net/~elmer-csc-ubuntu/+archive/ubuntu/elmer-csc-ppa), version 26.2, built from commit [`56b16bd49`](https://github.com/ElmerCSC/elmerfem/commit/56b16bd49564d5b16fdc57862ccda024043b0f39) of 2026-11-02, which is newer than the 26.2.1 release
- **One folder per machine and version:** results are kept by machine, and by the version of each code, so runs on different machines are never mixed. `make_history.py` plots FEAScript's speed-up by version for each benchmark and machine

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

The benchmarks in this repository are released under the [MIT license](LICENSE). Note that the core library of FEAScript is distributed under the terms of the [MIT license](https://github.com/FEAScript/FEAScript-core/blob/main/LICENSE).
