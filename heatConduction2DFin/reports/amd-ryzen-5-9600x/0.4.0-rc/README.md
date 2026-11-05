# Results for FEAScript 0.4.0-rc on AMD Ryzen 5 9600X 6-Core Processor

| | |
|---|---|
| FEAScript version | 0.4.0-rc |
| FEAScript commit | 7810802 |
| Released | not released |
| Loaded from | `dist/feascript.esm.js` |
| Elmer | 26.2 (build of commit `56b16bd49`, 2026-11-02) |
| scikit-fem | 12.0.2 (SciPy 1.18.1, NumPy 2.5.4, Python 3.12.3) |
| Node | v18.19.1 |
| Machine | AMD Ryzen 5 9600X 6-Core Processor, 14.7 GB RAM (Linux Mint 22.3, Linux 7.0.0-42-generic) |
| Cores | taskset -c 0, OMP_NUM_THREADS=1, OPENBLAS_NUM_THREADS=1 |
| Repeats | median of 5 fresh processes |
| Run on | 2026-11-05 |

All the numbers are in [results_table.md](results_table.md) and [results.json](results.json).

On every mesh it solved, FEAScript's nodal temperatures match Elmer's (UMFPACK) to within 5.0e-06 with the direct solvers (`frontal` and `lusolve`).

scikit-fem's nodal temperatures match FEAScript's (`lusolve`) to within 1.8e-10 and Elmer's (UMFPACK) to within 5.0e-06, the rounding of the 8 significant digits that Elmer writes its results with.

Where the Jacobi solver converged (residual tolerance 1e-8 within 10,000 iterations), its temperatures match Elmer's to within 1.9e-04: it stops at a residual tolerance, so its error grows with the mesh.

Runs that could not be measured:

- **FEAScript Jacobi, linear-80x40:** not converged
- **FEAScript Jacobi, linear-160x80:** not converged
- **FEAScript Jacobi, linear-320x160:** not converged
- **FEAScript Jacobi, quadratic-40x20:** not converged
- **FEAScript Jacobi, quadratic-80x40:** not converged
- **FEAScript Jacobi, quadratic-160x80:** not converged

## Accuracy

<img src="plots/accuracy.png" width="600" alt="RMS error against the exact solution">

## Assembly and solve time

<img src="plots/solve_time_linear.png" width="600" alt="Assembly and solve time with linear elements">
<img src="plots/solve_time_quadratic.png" width="600" alt="Assembly and solve time with quadratic elements">

## End-to-end time

<img src="plots/end_to_end.png" width="600" alt="End-to-end time on the 77×39 mesh">

## Peak memory

<img src="plots/memory_linear.png" width="600" alt="Peak memory with linear elements">
<img src="plots/memory_quadratic.png" width="600" alt="Peak memory with quadratic elements">

## Browsers

Chromium 156.0.8078.79, Firefox 159.0, each run in a fresh headless browser on one core, with FEAScript on the main thread of the page. The first solve in a fresh process on the largest mesh of each case, with the slowdown against Node.js:

| Case | Nodes | Node.js | Chromium | Firefox |
|---|---|---|---|---|
| FEAScript frontal, linear quads | 51,681 | 2.39 s | 1.58 s (0.7×) | 3.14 s (1.3×) |
| FEAScript sparse LU, linear quads | 51,681 | 2.00 s | 1.53 s (0.8×) | 21.75 s (10.9×) |

The solutions of the browsers differ from those of Node.js by at most 0.0e+00.

<img src="plots/browsers_FEAScript_frontal_linear_quads_first.png" width="600" alt="First solve: FEAScript frontal, linear quads">
<img src="plots/browsers_FEAScript_frontal_linear_quads_repeated.png" width="600" alt="Repeated solves: FEAScript frontal, linear quads">
<img src="plots/browsers_FEAScript_sparse_LU_linear_quads_first.png" width="600" alt="First solve: FEAScript sparse LU, linear quads">
<img src="plots/browsers_FEAScript_sparse_LU_linear_quads_repeated.png" width="600" alt="Repeated solves: FEAScript sparse LU, linear quads">
