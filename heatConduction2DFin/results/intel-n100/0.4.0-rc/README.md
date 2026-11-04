# Results for FEAScript 0.4.0-rc on Intel(R) N100

| | |
|---|---|
| FEAScript version | 0.4.0-rc |
| FEAScript commit | 933fb10 |
| Released | not released |
| Loaded from | `dist/feascript.esm.js` |
| Elmer | 26.2-unknown |
| Node | v18.19.1 |
| Machine | Intel(R) N100 (Linux 7.0.0-42-generic) |
| Cores | taskset -c 0, OMP_NUM_THREADS=1, OPENBLAS_NUM_THREADS=1 |
| Repeats | median of 5 fresh processes |
| Run on | 2026-11-04 |
| Note | Benchmarked from the working tree before it was committed as 933fb10 (frontal solver fix #121 and the math.js import change), with dist/ rebuilt from it |

All the numbers are in [results_table.md](results_table.md) and [results.json](results.json).

On every mesh it solved, FEAScript's nodal temperatures match Elmer's (UMFPACK) to within 5.0e-06.

## Accuracy

<img src="plots/accuracy.png" width="600" alt="RMS error against the exact solution">

## Assembly and solve time

<img src="plots/solve_time_linear.png" width="600" alt="Assembly and solve time with linear elements">
<img src="plots/solve_time_quadratic.png" width="600" alt="Assembly and solve time with quadratic elements">

## End-to-end time

<img src="plots/end_to_end.png" width="600" alt="End-to-end time on the 77×39 mesh">
