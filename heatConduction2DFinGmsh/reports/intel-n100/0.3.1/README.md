# Results for FEAScript 0.3.1 on Intel(R) N100

| | |
|---|---|
| FEAScript version | 0.3.1 |
| FEAScript commit | 083fc8c |
| Released | 2026-10-30 |
| Loaded from | `dist/feascript.esm.js` |
| Elmer | 26.2 |
| scikit-fem | 12.0.2 (SciPy 1.18.1, NumPy 2.5.4, meshio 5.3.5, Python 3.12.3) |
| Gmsh | 4.12.1 |
| Node | v18.19.1 |
| Machine | Intel(R) N100, 7.5 GB RAM (Linux Mint 22.3, Linux 7.0.0-42-generic) |
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

Repeated solves that were not run, because the first solve took over 20 s and the case was timed once:

- **FEAScript frontal, tri-linear-h0.05**
- **FEAScript frontal, tri-quadratic-h0.1**
- **FEAScript frontal, quad-quadratic-h0.2**

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
| FEAScript frontal, quadratic triangles | 3,857 | 27.73 s | 45.41 s (1.6×) | 79.21 s (2.9×) |
| FEAScript sparse LU, quadratic triangles | 59,885 | 12.43 s | 9.88 s (0.8×) | 191.02 s (15.4×) |
| FEAScript frontal, quadratic quadrilaterals | 5,953 | 153.52 s | 146.44 s (1.0×) | 280.97 s (1.8×) |
| FEAScript sparse LU, quadratic quadrilaterals | 89,209 | 8.43 s | 6.37 s (0.8×) | 111.87 s (13.3×) |

The browsers give the same solutions as Node.js, bit for bit. Cases with a first solve over 20 s are timed once, with one repeated solve in the browsers and none in Node.js, instead of five times with three repeated solves. A case without a point on a plot was not measured, and each such case is listed in this report.

<img src="plots/browsers_FEAScript_frontal_quadratic_triangles_first.png" width="600" alt="First solve: FEAScript frontal, quadratic triangles">
<img src="plots/browsers_FEAScript_frontal_quadratic_triangles_repeated.png" width="600" alt="Repeated solves: FEAScript frontal, quadratic triangles">
<img src="plots/browsers_FEAScript_sparse_LU_quadratic_triangles_first.png" width="600" alt="First solve: FEAScript sparse LU, quadratic triangles">
<img src="plots/browsers_FEAScript_sparse_LU_quadratic_triangles_repeated.png" width="600" alt="Repeated solves: FEAScript sparse LU, quadratic triangles">
<img src="plots/browsers_FEAScript_frontal_quadratic_quadrilaterals_first.png" width="600" alt="First solve: FEAScript frontal, quadratic quadrilaterals">
<img src="plots/browsers_FEAScript_frontal_quadratic_quadrilaterals_repeated.png" width="600" alt="Repeated solves: FEAScript frontal, quadratic quadrilaterals">
<img src="plots/browsers_FEAScript_sparse_LU_quadratic_quadrilaterals_first.png" width="600" alt="First solve: FEAScript sparse LU, quadratic quadrilaterals">
<img src="plots/browsers_FEAScript_sparse_LU_quadratic_quadrilaterals_repeated.png" width="600" alt="Repeated solves: FEAScript sparse LU, quadratic quadrilaterals">
