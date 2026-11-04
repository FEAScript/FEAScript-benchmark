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

All the numbers are in [results_table.md](results_table.md) and [results.json](results.json).

On every mesh it solved, FEAScript's primary vortex strength ψ_min matches Elmer's (UMFPACK) to within 1.2e-04.

At the nodes farther than 0.2 from the two lid corners, the velocities of the two codes differ by at most 4.9e-05 on the 64×64 mesh, against 8.0e-02 on the 8×8 mesh, so both converge to the same solution. Next to the lid corners they differ by up to 0.17 on every mesh: there FEAScript applies the full lid velocity along the top edge of the corner element, while Elmer interpolates it linearly from the corner, where the velocity is 0.

## Primary vortex strength

<img src="plots/psi_min.png" width="600" alt="Primary vortex strength against the mesh">

## Centerline velocity

<img src="plots/centerline.png" width="600" alt="Velocity along the vertical centerline">

## Assembly and solve time

<img src="plots/solve_time.png" width="600" alt="Assembly and solve time against the number of nodes">

## End-to-end time

<img src="plots/end_to_end.png" width="600" alt="End-to-end time on the 16×16 mesh">
