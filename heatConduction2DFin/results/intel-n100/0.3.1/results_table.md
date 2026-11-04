| case | nodes | code | solve | linsolve | process | warmWall | rmsErr | maxErr | maxDiffVsElmerUMFPACK | nruns |
|---|---|---|---|---|---|---|---|---|---|---|
| linear-20x10 | 231 | FEAScript frontal | 0.36 | 0.353 | 0.633 | 0.356 | 0.113 | 1.02 | 4.96e-06 | 5 |
| linear-20x10 | 231 | FEAScript sparse LU | 0.176 | 0.152 | 0.483 | 0.0687 | 0.113 | 1.02 | 4.96e-06 | 5 |
| linear-20x10 | 231 | Elmer BiCGStab+ILU0 | 0 | 0 | 2.06 |  | 0.113 | 1.02 | 1e-06 | 5 |
| linear-20x10 | 231 | Elmer UMFPACK | 0 | 0 | 2.06 |  | 0.113 | 1.02 | 0 | 5 |
| linear-20x10 | 231 | Elmer MUMPS | 0 | 0 | 2.08 |  | 0.113 | 1.02 | 0 | 5 |
| linear-40x20 | 861 | FEAScript frontal | 0.425 | 0.416 | 0.668 | 0.421 | 0.0316 | 0.574 | 4.99e-06 | 5 |
| linear-40x20 | 861 | FEAScript sparse LU | 0.26 | 0.222 | 0.487 | 0.14 | 0.0316 | 0.574 | 4.99e-06 | 5 |
| linear-40x20 | 861 | Elmer BiCGStab+ILU0 | 0.01 | 0 | 2.05 |  | 0.0316 | 0.574 | 1e-05 | 5 |
| linear-40x20 | 861 | Elmer UMFPACK | 0.01 | 0 | 2.05 |  | 0.0316 | 0.574 | 0 | 5 |
| linear-40x20 | 861 | Elmer MUMPS | 0.01 | 0 | 2.08 |  | 0.0316 | 0.574 | 0 | 5 |
| linear-80x40 | 3321 | FEAScript frontal | 1.06 | 1.03 | 1.33 | 0.984 | 0.00883 | 0.307 | 5e-06 | 5 |
| linear-80x40 | 3321 | FEAScript sparse LU | 0.549 | 0.492 | 0.783 | 0.513 | 0.00883 | 0.307 | 5e-06 | 5 |
| linear-80x40 | 3321 | Elmer BiCGStab+ILU0 | 0.03 | 0.01 | 2.08 |  | 0.00883 | 0.307 | 1e-05 | 5 |
| linear-80x40 | 3321 | Elmer UMFPACK | 0.02 | 0.01 | 2.09 |  | 0.00883 | 0.307 | 0 | 5 |
| linear-80x40 | 3321 | Elmer MUMPS | 0.02 | 0.01 | 2.08 |  | 0.00883 | 0.307 | 0 | 5 |
| linear-160x80 | 13041 | FEAScript frontal | 40.9 | 40.8 | 135 | 31.4 | 0.00244 | 0.159 | 5e-06 | 1 |
| linear-160x80 | 13041 | FEAScript sparse LU | 1.32 | 1.22 | 1.56 | 1.66 | 0.00244 | 0.159 | 5e-06 | 5 |
| linear-160x80 | 13041 | Elmer BiCGStab+ILU0 | 0.15 | 0.11 | 2.24 |  | 0.00244 | 0.159 | 1e-05 | 5 |
| linear-160x80 | 13041 | Elmer UMFPACK | 0.1 | 0.05 | 2.17 |  | 0.00244 | 0.159 | 0 | 5 |
| linear-160x80 | 13041 | Elmer MUMPS | 0.11 | 0.07 | 2.18 |  | 0.00244 | 0.159 | 0 | 5 |
| linear-320x160 |  | FEAScript frontal | out of memory |  |  |  |  |  |  |  |
| linear-320x160 | 51681 | FEAScript sparse LU | 5.7 | 5.32 | 5.98 | 10.4 | 0.000666 | 0.0812 | 5e-06 | 5 |
| linear-320x160 | 51681 | Elmer BiCGStab+ILU0 | 1.06 | 0.87 | 3.25 |  | 0.000666 | 0.0812 | 3e-05 | 5 |
| linear-320x160 | 51681 | Elmer UMFPACK | 0.53 | 0.33 | 2.72 |  | 0.000666 | 0.0812 | 0 | 5 |
| linear-320x160 | 51681 | Elmer MUMPS | 0.49 | 0.31 | 2.68 |  | 0.000666 | 0.0812 | 0 | 5 |
| linear-77x39 | 3120 | FEAScript frontal | 0.84 | 0.817 | 1.05 | 0.779 | 0.00938 | 0.312 | 5e-06 | 5 |
| linear-77x39 | 3120 | FEAScript sparse LU | 0.445 | 0.393 | 0.65 | 0.464 | 0.00938 | 0.312 | 5e-06 | 5 |
| linear-77x39 | 3120 | Elmer BiCGStab+ILU0 | 0.02 | 0.01 | 2.07 |  | 0.00938 | 0.312 | 1e-05 | 5 |
| linear-77x39 | 3120 | Elmer UMFPACK | 0.02 | 0.01 | 2.07 |  | 0.00938 | 0.312 | 0 | 5 |
| linear-77x39 | 3120 | Elmer MUMPS | 0.02 | 0.01 | 2.1 |  | 0.00938 | 0.312 | 0 | 5 |
| quadratic-10x5 | 231 | FEAScript frontal | 0.55 | 0.544 | 0.772 | 0.43 | 0.0667 | 0.8 | 4.99e-06 | 5 |
| quadratic-10x5 | 231 | FEAScript sparse LU | 0.162 | 0.139 | 0.425 | 0.0816 | 0.0667 | 0.8 | 4.99e-06 | 5 |
| quadratic-10x5 | 231 | Elmer BiCGStab+ILU0 | 0 | 0 | 2.09 |  | 0.0667 | 0.8 | 1e-05 | 5 |
| quadratic-10x5 | 231 | Elmer UMFPACK | 0 | 0 | 2.05 |  | 0.0667 | 0.8 | 0 | 5 |
| quadratic-10x5 | 231 | Elmer MUMPS | 0 | 0 | 2.05 |  | 0.0667 | 0.8 | 0 | 5 |
| quadratic-20x10 | 861 | FEAScript frontal | 1.1 | 1.1 | 1.34 | 0.985 | 0.0169 | 0.394 | 4.99e-06 | 5 |
| quadratic-20x10 | 861 | FEAScript sparse LU | 0.279 | 0.236 | 0.505 | 0.173 | 0.0169 | 0.394 | 4.99e-06 | 5 |
| quadratic-20x10 | 861 | Elmer BiCGStab+ILU0 | 0.01 | 0 | 2.05 |  | 0.0169 | 0.394 | 1e-06 | 5 |
| quadratic-20x10 | 861 | Elmer UMFPACK | 0.01 | 0 | 2.1 |  | 0.0169 | 0.394 | 0 | 5 |
| quadratic-20x10 | 861 | Elmer MUMPS | 0.01 | 0 | 2.11 |  | 0.0169 | 0.394 | 0 | 5 |
| quadratic-40x20 | 3321 | FEAScript frontal | 38.4 | 38.4 | 143 | 29.1 | 0.00426 | 0.196 | 5e-06 | 1 |
| quadratic-40x20 | 3321 | FEAScript sparse LU | 0.74 | 0.649 | 1.11 | 0.786 | 0.00426 | 0.196 | 5e-06 | 5 |
| quadratic-40x20 | 3321 | Elmer BiCGStab+ILU0 | 0.03 | 0.02 | 2.18 |  | 0.00426 | 0.196 | 1e-05 | 5 |
| quadratic-40x20 | 3321 | Elmer UMFPACK | 0.03 | 0.02 | 2.17 |  | 0.00426 | 0.196 | 0 | 5 |
| quadratic-40x20 | 3321 | Elmer MUMPS | 0.03 | 0.02 | 2.3 |  | 0.00426 | 0.196 | 0 | 5 |
| quadratic-80x40 |  | FEAScript frontal | out of memory |  |  |  |  |  |  |  |
| quadratic-80x40 | 13041 | FEAScript sparse LU | 1.39 | 1.28 | 1.64 | 1.92 | 0.00107 | 0.0975 | 5e-06 | 5 |
| quadratic-80x40 | 13041 | Elmer BiCGStab+ILU0 | 0.16 | 0.12 | 2.32 |  | 0.00107 | 0.0975 | 1e-05 | 5 |
| quadratic-80x40 | 13041 | Elmer UMFPACK | 0.1 | 0.06 | 2.26 |  | 0.00107 | 0.0975 | 0 | 5 |
| quadratic-80x40 | 13041 | Elmer MUMPS | 0.12 | 0.08 | 2.27 |  | 0.00107 | 0.0975 | 0 | 5 |
| quadratic-160x80 |  | FEAScript frontal | out of memory |  |  |  |  |  |  |  |
| quadratic-160x80 | 51681 | FEAScript sparse LU | 5.97 | 5.64 | 6.23 | 10.8 | 0.000268 | 0.0487 | 5e-06 | 5 |
| quadratic-160x80 | 51681 | Elmer BiCGStab+ILU0 | 1.21 | 1.07 | 3.72 |  | 0.000268 | 0.0487 | 1e-05 | 5 |
| quadratic-160x80 | 51681 | Elmer UMFPACK | 0.64 | 0.51 | 3.17 |  | 0.000268 | 0.0487 | 0 | 5 |
| quadratic-160x80 | 51681 | Elmer MUMPS | 0.52 | 0.38 | 3.08 |  | 0.000268 | 0.0487 | 1e-06 | 5 |
