# Results for FEAScript 0.3.1 on AMD Ryzen 5 9600X 6-Core Processor

| | |
|---|---|
| FEAScript version | 0.3.1 |
| FEAScript commit | 083fc8c |
| Released | 2026-10-30 |
| Loaded from | `dist/feascript.esm.js` |
| Elmer | 26.2 (build of commit `56b16bd49`, 2026-11-02) |
| scikit-fem | 12.0.2 (SciPy 1.18.1, NumPy 2.5.4, meshio 5.3.5, Python 3.12.3) |
| Gmsh | 4.12.1 |
| Node | v18.19.1 |
| Machine | AMD Ryzen 5 9600X 6-Core Processor, 14.7 GB RAM (Linux Mint 22.3, Linux 7.0.0-42-generic) |
| Cores | taskset -c 0, OMP_NUM_THREADS=1, OPENBLAS_NUM_THREADS=1 |
| Repeats | median of 5 fresh processes |
| Run on | 2026-11-06 |

All the numbers are in [results_table.md](results_table.md) and [results.json](results.json).

On every mesh it solved, with triangles and quadrilaterals, FEAScript's nodal temperatures match scikit-fem's to within 1.2e-10 when scikit-fem uses the same Gauss rules, and Elmer's (UMFPACK) to within 5.0e-06, the rounding of the 8 significant digits that Elmer writes its results with. The `frontal` and `lusolve` solvers agree to within 2.2e-10.

On distorted quadrilaterals these Gauss rules are not exact. With a much finer rule, scikit-fem's RMS error is lower than FEAScript's by 1.2% to 2.1%. On triangles the rules are exact, so the finer rule changes nothing.

Runs that could not be measured:

- **FEAScript frontal, tri-linear-h0.025:** out of memory
- **FEAScript frontal, tri-quadratic-h0.05:** out of memory
- **FEAScript frontal, tri-quadratic-h0.025:** out of memory
- **FEAScript frontal, quad-linear-h0.05:** out of memory
- **FEAScript frontal, quad-quadratic-h0.1:** out of memory
- **FEAScript frontal, quad-quadratic-h0.05:** out of memory

## Accuracy

<img src="plots/accuracy_tri.png" width="600" alt="RMS error against the exact solution on triangles">
<img src="plots/accuracy_quad.png" width="600" alt="RMS error against the exact solution on quadrilaterals">

## Assembly and solve time

<img src="plots/solve_time_tri_linear.png" width="600" alt="Assembly and solve time, linear triangles">
<img src="plots/solve_time_tri_quadratic.png" width="600" alt="Assembly and solve time, quadratic triangles">
<img src="plots/solve_time_quad_linear.png" width="600" alt="Assembly and solve time, linear quadrilaterals">
<img src="plots/solve_time_quad_quadratic.png" width="600" alt="Assembly and solve time, quadratic quadrilaterals">

## Peak memory

<img src="plots/memory_tri_linear.png" width="600" alt="Peak memory, linear triangles">
<img src="plots/memory_tri_quadratic.png" width="600" alt="Peak memory, quadratic triangles">
<img src="plots/memory_quad_linear.png" width="600" alt="Peak memory, linear quadrilaterals">
<img src="plots/memory_quad_quadratic.png" width="600" alt="Peak memory, quadratic quadrilaterals">

## Browsers

Chromium 156.0.8078.79, Firefox 159.0, each run in a fresh headless browser on one core, with FEAScript on the main thread of the page. The first solve in a fresh process on the largest mesh of each case, with the slowdown against Node.js:

| Case | Nodes | Node.js | Chromium | Firefox |
|---|---|---|---|---|
| FEAScript frontal, quadratic triangles | 3,857 | 11.19 s | 10.24 s (0.9×) | 15.66 s (1.4×) |
| FEAScript sparse LU, quadratic triangles | 59,885 | 5.07 s | 4.00 s (0.8×) | 78.45 s (15.5×) |
| FEAScript frontal, quadratic quadrilaterals | 5,953 | 60.80 s | 63.44 s (1.0×) | 90.98 s (1.5×) |
| FEAScript sparse LU, quadratic quadrilaterals | 89,209 | 3.50 s | 2.63 s (0.8×) | 33.99 s (9.7×) |

The solutions of the browsers differ from those of Node.js by at most 0.0e+00. Cases with a first solve over 20 s are timed once, with one repeated solve, instead of five times with three repeated solves. A case without a point on a plot was not measured.

<img src="plots/browsers_FEAScript_frontal_quadratic_triangles_first.png" width="600" alt="First solve: FEAScript frontal, quadratic triangles">
<img src="plots/browsers_FEAScript_frontal_quadratic_triangles_repeated.png" width="600" alt="Repeated solves: FEAScript frontal, quadratic triangles">
<img src="plots/browsers_FEAScript_sparse_LU_quadratic_triangles_first.png" width="600" alt="First solve: FEAScript sparse LU, quadratic triangles">
<img src="plots/browsers_FEAScript_sparse_LU_quadratic_triangles_repeated.png" width="600" alt="Repeated solves: FEAScript sparse LU, quadratic triangles">
<img src="plots/browsers_FEAScript_frontal_quadratic_quadrilaterals_first.png" width="600" alt="First solve: FEAScript frontal, quadratic quadrilaterals">
<img src="plots/browsers_FEAScript_frontal_quadratic_quadrilaterals_repeated.png" width="600" alt="Repeated solves: FEAScript frontal, quadratic quadrilaterals">
<img src="plots/browsers_FEAScript_sparse_LU_quadratic_quadrilaterals_first.png" width="600" alt="First solve: FEAScript sparse LU, quadratic quadrilaterals">
<img src="plots/browsers_FEAScript_sparse_LU_quadratic_quadrilaterals_repeated.png" width="600" alt="Repeated solves: FEAScript sparse LU, quadratic quadrilaterals">
