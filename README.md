<img src="https://feascript.github.io/FEAScript-website/assets/feascript-logo.png" width="80" alt="FEAScript Logo">

# FEAScript-benchmark

This repository contains benchmarks for [FEAScript](https://feascript.com/), the finite element simulation library developed in JavaScript. Each benchmark runs FEAScript and an established finite element solver on the same problem and compares them on accuracy and run time, against an exact solution where one exists. Results are kept for every machine and FEAScript version, so the comparison can be followed as FEAScript develops.

<img src="heatConduction2DFin/history/intel-n100/linear-160x80.png" width="500" alt="FEAScript speed-up by version">

## Benchmarks

| Benchmark | Compared with | Problem |
|---|---|---|
| [heatConduction2DFin](heatConduction2DFin/) | [Elmer](https://www.elmerfem.org/) | 2D heat conduction in a fin with constant-temperature, symmetry and convection boundaries, on linear and quadratic quadrilateral meshes from 231 to 51,681 nodes |
| [creepingFlow2DLidDrivenCavity](creepingFlow2DLidDrivenCavity/) | [Elmer](https://www.elmerfem.org/) | Stokes (creeping) flow in the lid-driven unit cavity, with Taylor–Hood Q2–Q1 elements on meshes from 289 to 16,641 velocity nodes |

📖 Each benchmark folder has a README with the problem, the setup, the results and the steps to run it.

## How the benchmarks are run

- **Same problem, same meshes:** both codes solve identical meshes, so their nodal results can be compared one to one
- **One core:** every timed process is pinned to one core, so neither code gains from multithreading
- **Fresh processes:** each timing is the median of several fresh processes
- **FEAScript as users load it:** the benchmarks load the built bundle `dist/feascript.esm.js` from a [FEAScript-core](https://github.com/FEAScript/FEAScript-core) checkout, by default the sibling folder `../FEAScript-core`
- **Recorded setup:** each run writes a `meta.json` with the FEAScript version and commit, the versions of the other software, the machine and the date
- **One folder per machine and version:** results are kept in `results/<machine>/<version>/`, so runs on different machines are never mixed. `make_history.py` plots FEAScript's speed-up by version for each benchmark and machine

## About the comparison

These benchmarks use [Elmer](https://www.elmerfem.org/), the open-source multiphysics finite element software developed by CSC – IT Center for Science, as a trusted reference for checking and tracking FEAScript. They are not a ranking of the two programs, which are built for very different purposes:

- **Elmer** is a mature, parallel code for large multiphysics problems, typically in 3D. It runs on many cores and across many machines with MPI and OpenMP, and offers a wide range of solvers and preconditioners for large systems
- **FEAScript** is a JavaScript library that runs in a single thread of a web browser or Node.js, for small and medium problems, teaching and web applications

To compare the two codes on the same terms, the benchmarks run Elmer the way FEAScript runs: on one core, as a single MPI process, on small 2D problems. This is not how Elmer is meant to be used for large problems, and its parallel performance is not measured here. Keep in mind when reading the results:

- **Solver speed:** Elmer assembles and solves these problems roughly 10 times faster than FEAScript on the larger meshes, on one core
- **End-to-end time:** on small meshes FEAScript can finish first, because the Elmer build used here (an MPI-enabled build) spends about 2 s starting MPI at the beginning of every run, even with one process. This is a fixed start-up cost, not solver speed, and it becomes negligible for the larger problems Elmer is designed for
- **Elmer settings:** the Elmer cases use standard settings and solvers (UMFPACK, MUMPS, BiCGStab with ILU0) chosen by the FEAScript team, not tuned by Elmer experts. Other settings may well make Elmer faster
- **Timer resolution:** Elmer reports its solver time to 0.01 s, so its times on the smallest meshes are rounded

We are grateful to the Elmer developers for making such capable software freely available.

## License

The benchmarks in this repository are released under the [MIT license](LICENSE). Note that the core library of FEAScript is distributed under the terms of the [MIT license](https://github.com/FEAScript/FEAScript-core/blob/main/LICENSE).
