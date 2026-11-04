| case | nodes | code | solve | linsolve | process | warmWall | rmsErr | maxErr | maxDiffVsElmerUMFPACK | nruns |
|---|---|---|---|---|---|---|---|---|---|---|
| linear-20x10 | 231 | FEAScript frontal | 0.0477 | 0.0431 | 0.246 | 0.0337 | 0.113 | 1.02 | 4.96e-06 | 5 |
| linear-20x10 | 231 | FEAScript sparse LU | 0.147 | 0.129 | 0.325 | 0.0416 | 0.113 | 1.02 | 4.96e-06 | 5 |
| linear-20x10 | 231 | Elmer BiCGStab+ILU0 | 0 | 0 | 2.05 |  | 0.113 | 1.02 | 1e-06 | 5 |
| linear-20x10 | 231 | Elmer UMFPACK | 0 | 0 | 2.05 |  | 0.113 | 1.02 | 0 | 5 |
| linear-20x10 | 231 | Elmer MUMPS | 0 | 0 | 2.05 |  | 0.113 | 1.02 | 0 | 5 |
| linear-40x20 | 861 | FEAScript frontal | 0.235 | 0.229 | 0.444 | 0.0986 | 0.0316 | 0.574 | 4.99e-06 | 5 |
| linear-40x20 | 861 | FEAScript sparse LU | 0.26 | 0.218 | 0.451 | 0.176 | 0.0316 | 0.574 | 4.99e-06 | 5 |
| linear-40x20 | 861 | Elmer BiCGStab+ILU0 | 0.01 | 0 | 2.04 |  | 0.0316 | 0.574 | 1e-05 | 5 |
| linear-40x20 | 861 | Elmer UMFPACK | 0.01 | 0 | 2.06 |  | 0.0316 | 0.574 | 0 | 5 |
| linear-40x20 | 861 | Elmer MUMPS | 0.01 | 0 | 2.06 |  | 0.0316 | 0.574 | 0 | 5 |
| linear-80x40 | 3321 | FEAScript frontal | 0.301 | 0.284 | 0.507 | 0.174 | 0.00883 | 0.307 | 5e-06 | 5 |
| linear-80x40 | 3321 | FEAScript sparse LU | 0.475 | 0.428 | 0.675 | 0.527 | 0.00883 | 0.307 | 5e-06 | 5 |
| linear-80x40 | 3321 | Elmer BiCGStab+ILU0 | 0.03 | 0.01 | 2.07 |  | 0.00883 | 0.307 | 1e-05 | 5 |
| linear-80x40 | 3321 | Elmer UMFPACK | 0.02 | 0.01 | 2.09 |  | 0.00883 | 0.307 | 0 | 5 |
| linear-80x40 | 3321 | Elmer MUMPS | 0.02 | 0.01 | 2.07 |  | 0.00883 | 0.307 | 0 | 5 |
| linear-160x80 | 13041 | FEAScript frontal | 0.885 | 0.84 | 1.07 | 0.669 | 0.00244 | 0.159 | 5e-06 | 5 |
| linear-160x80 | 13041 | FEAScript sparse LU | 1.27 | 1.17 | 1.47 | 1.74 | 0.00244 | 0.159 | 5e-06 | 5 |
| linear-160x80 | 13041 | Elmer BiCGStab+ILU0 | 0.15 | 0.11 | 2.22 |  | 0.00244 | 0.159 | 1e-05 | 5 |
| linear-160x80 | 13041 | Elmer UMFPACK | 0.1 | 0.05 | 2.17 |  | 0.00244 | 0.159 | 0 | 5 |
| linear-160x80 | 13041 | Elmer MUMPS | 0.12 | 0.07 | 2.19 |  | 0.00244 | 0.159 | 0 | 5 |
| linear-320x160 | 51681 | FEAScript frontal | 6.44 | 6.29 | 6.82 | 5.98 | 0.000666 | 0.0812 | 5e-06 | 5 |
| linear-320x160 | 51681 | FEAScript sparse LU | 5.14 | 4.88 | 5.62 | 9.67 | 0.000666 | 0.0812 | 5e-06 | 5 |
| linear-320x160 | 51681 | Elmer BiCGStab+ILU0 | 1.06 | 0.88 | 3.26 |  | 0.000666 | 0.0812 | 3e-05 | 5 |
| linear-320x160 | 51681 | Elmer UMFPACK | 0.55 | 0.33 | 2.79 |  | 0.000666 | 0.0812 | 0 | 5 |
| linear-320x160 | 51681 | Elmer MUMPS | 0.54 | 0.33 | 2.76 |  | 0.000666 | 0.0812 | 0 | 5 |
| linear-77x39 | 3120 | FEAScript frontal | 0.346 | 0.33 | 0.559 | 0.174 | 0.00938 | 0.312 | 5e-06 | 5 |
| linear-77x39 | 3120 | FEAScript sparse LU | 0.551 | 0.494 | 0.784 | 0.495 | 0.00938 | 0.312 | 5e-06 | 5 |
| linear-77x39 | 3120 | Elmer BiCGStab+ILU0 | 0.03 | 0.01 | 2.09 |  | 0.00938 | 0.312 | 1e-05 | 5 |
| linear-77x39 | 3120 | Elmer UMFPACK | 0.02 | 0.01 | 2.12 |  | 0.00938 | 0.312 | 0 | 5 |
| linear-77x39 | 3120 | Elmer MUMPS | 0.02 | 0.01 | 2.08 |  | 0.00938 | 0.312 | 0 | 5 |
| quadratic-10x5 | 231 | FEAScript frontal | 0.0507 | 0.0463 | 0.241 | 0.0481 | 0.0667 | 0.8 | 4.99e-06 | 5 |
| quadratic-10x5 | 231 | FEAScript sparse LU | 0.165 | 0.14 | 0.352 | 0.0564 | 0.0667 | 0.8 | 4.99e-06 | 5 |
| quadratic-10x5 | 231 | Elmer BiCGStab+ILU0 | 0 | 0 | 2.05 |  | 0.0667 | 0.8 | 1e-05 | 5 |
| quadratic-10x5 | 231 | Elmer UMFPACK | 0 | 0 | 2.07 |  | 0.0667 | 0.8 | 0 | 5 |
| quadratic-10x5 | 231 | Elmer MUMPS | 0 | 0 | 2.06 |  | 0.0667 | 0.8 | 0 | 5 |
| quadratic-20x10 | 861 | FEAScript frontal | 0.349 | 0.342 | 0.579 | 0.0867 | 0.0169 | 0.394 | 4.99e-06 | 5 |
| quadratic-20x10 | 861 | FEAScript sparse LU | 0.278 | 0.236 | 0.543 | 0.173 | 0.0169 | 0.394 | 4.99e-06 | 5 |
| quadratic-20x10 | 861 | Elmer BiCGStab+ILU0 | 0.01 | 0 | 2.06 |  | 0.0169 | 0.394 | 1e-06 | 5 |
| quadratic-20x10 | 861 | Elmer UMFPACK | 0.01 | 0 | 2.13 |  | 0.0169 | 0.394 | 0 | 5 |
| quadratic-20x10 | 861 | Elmer MUMPS | 0.01 | 0 | 2.1 |  | 0.0169 | 0.394 | 0 | 5 |
| quadratic-40x20 | 3321 | FEAScript frontal | 0.382 | 0.369 | 0.575 | 0.165 | 0.00426 | 0.196 | 5e-06 | 5 |
| quadratic-40x20 | 3321 | FEAScript sparse LU | 0.573 | 0.516 | 0.769 | 0.535 | 0.00426 | 0.196 | 5e-06 | 5 |
| quadratic-40x20 | 3321 | Elmer BiCGStab+ILU0 | 0.03 | 0.02 | 2.11 |  | 0.00426 | 0.196 | 1e-05 | 5 |
| quadratic-40x20 | 3321 | Elmer UMFPACK | 0.03 | 0.01 | 2.14 |  | 0.00426 | 0.196 | 0 | 5 |
| quadratic-40x20 | 3321 | Elmer MUMPS | 0.02 | 0.01 | 2.1 |  | 0.00426 | 0.196 | 0 | 5 |
| quadratic-80x40 | 13041 | FEAScript frontal | 0.791 | 0.765 | 0.966 | 0.503 | 0.00107 | 0.0975 | 5e-06 | 5 |
| quadratic-80x40 | 13041 | FEAScript sparse LU | 1.34 | 1.24 | 1.54 | 1.75 | 0.00107 | 0.0975 | 5e-06 | 5 |
| quadratic-80x40 | 13041 | Elmer BiCGStab+ILU0 | 0.16 | 0.12 | 2.32 |  | 0.00107 | 0.0975 | 1e-05 | 5 |
| quadratic-80x40 | 13041 | Elmer UMFPACK | 0.1 | 0.07 | 2.27 |  | 0.00107 | 0.0975 | 0 | 5 |
| quadratic-80x40 | 13041 | Elmer MUMPS | 0.12 | 0.08 | 2.28 |  | 0.00107 | 0.0975 | 0 | 5 |
| quadratic-160x80 | 51681 | FEAScript frontal | 4.93 | 4.83 | 5.29 | 5.15 | 0.000268 | 0.0487 | 5e-06 | 5 |
| quadratic-160x80 | 51681 | FEAScript sparse LU | 5.79 | 5.5 | 5.99 | 11.6 | 0.000268 | 0.0487 | 5e-06 | 5 |
| quadratic-160x80 | 51681 | Elmer BiCGStab+ILU0 | 1.19 | 1.06 | 3.71 |  | 0.000268 | 0.0487 | 1e-05 | 5 |
| quadratic-160x80 | 51681 | Elmer UMFPACK | 0.64 | 0.51 | 3.16 |  | 0.000268 | 0.0487 | 0 | 5 |
| quadratic-160x80 | 51681 | Elmer MUMPS | 0.5 | 0.37 | 3.01 |  | 0.000268 | 0.0487 | 1e-06 | 5 |
