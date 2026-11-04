| case | nodes | code | solve | linsolve | process | warmWall | rmsErr | maxErr | maxDiffVsElmerUMFPACK | nruns |
|---|---|---|---|---|---|---|---|---|---|---|
| linear-20x10 | 231 | FEAScript frontal | 0.229 | 0.22 | 2.34 | 0.287 | 0.646 | 6.07 | 5.08 | 5 |
| linear-20x10 | 231 | FEAScript sparse LU | 0.0879 | 0.076 | 2.15 | 0.049 | 0.646 | 6.07 | 5.08 | 5 |
| linear-20x10 | 231 | Elmer BiCGStab+ILU0 | 0 | 0 | 2.04 |  | 0.113 | 1.02 | 1e-06 | 5 |
| linear-20x10 | 231 | Elmer UMFPACK | 0 | 0 | 2.06 |  | 0.113 | 1.02 | 0 | 5 |
| linear-20x10 | 231 | Elmer MUMPS | 0 | 0 | 2.05 |  | 0.113 | 1.02 | 0 | 5 |
| linear-40x20 | 861 | FEAScript frontal | 0.33 | 0.302 | 2.6 | 0.335 | 0.186 | 3.08 | 2.66 | 5 |
| linear-40x20 | 861 | FEAScript sparse LU | 0.228 | 0.18 | 2.44 | 0.211 | 0.186 | 3.08 | 2.66 | 5 |
| linear-40x20 | 861 | Elmer BiCGStab+ILU0 | 0.01 | 0 | 2.04 |  | 0.0316 | 0.574 | 1e-05 | 5 |
| linear-40x20 | 861 | Elmer UMFPACK | 0.01 | 0 | 2.04 |  | 0.0316 | 0.574 | 0 | 5 |
| linear-40x20 | 861 | Elmer MUMPS | 0.01 | 0 | 2.05 |  | 0.0316 | 0.574 | 0 | 5 |
| linear-80x40 | 3321 | FEAScript frontal | 1.08 | 0.805 | 3.13 | 1.02 | 0.0515 | 1.55 | 1.36 | 5 |
| linear-80x40 | 3321 | FEAScript sparse LU | 1.34 | 0.882 | 3.44 | 1.34 | 0.0515 | 1.55 | 1.36 | 5 |
| linear-80x40 | 3321 | Elmer BiCGStab+ILU0 | 0.03 | 0.01 | 2.07 |  | 0.00883 | 0.307 | 1e-05 | 5 |
| linear-80x40 | 3321 | Elmer UMFPACK | 0.02 | 0.01 | 2.08 |  | 0.00883 | 0.307 | 0 | 5 |
| linear-80x40 | 3321 | Elmer MUMPS | 0.02 | 0.01 | 2.06 |  | 0.00883 | 0.307 | 0 | 5 |
| linear-160x80 |  | FEAScript frontal | out of memory |  |  |  |  |  |  |  |
| linear-160x80 | 13041 | FEAScript sparse LU | 45.4 | 37.4 | 191 | 48.2 | 0.0139 | 0.774 | 0.691 | 1 |
| linear-160x80 | 13041 | Elmer BiCGStab+ILU0 | 0.16 | 0.11 | 2.23 |  | 0.00244 | 0.159 | 1e-05 | 5 |
| linear-160x80 | 13041 | Elmer UMFPACK | 0.1 | 0.05 | 2.18 |  | 0.00244 | 0.159 | 0 | 5 |
| linear-160x80 | 13041 | Elmer MUMPS | 0.12 | 0.07 | 2.19 |  | 0.00244 | 0.159 | 0 | 5 |
| linear-320x160 |  | FEAScript frontal | out of memory |  |  |  |  |  |  |  |
| linear-320x160 |  | FEAScript sparse LU | out of memory |  |  |  |  |  |  |  |
| linear-320x160 | 51681 | Elmer BiCGStab+ILU0 | 1.03 | 0.86 | 3.21 |  | 0.000666 | 0.0812 | 3e-05 | 5 |
| linear-320x160 | 51681 | Elmer UMFPACK | 0.48 | 0.3 | 2.66 |  | 0.000666 | 0.0812 | 0 | 5 |
| linear-320x160 | 51681 | Elmer MUMPS | 0.55 | 0.34 | 2.81 |  | 0.000666 | 0.0812 | 0 | 5 |
| linear-77x39 | 3120 | FEAScript frontal | 1.04 | 0.749 | 3.44 | 1.14 | 0.0548 | 1.61 | 1.41 | 5 |
| linear-77x39 | 3120 | FEAScript sparse LU | 1.13 | 0.73 | 2.97 | 1.23 | 0.0548 | 1.61 | 1.41 | 5 |
| linear-77x39 | 3120 | Elmer BiCGStab+ILU0 | 0.02 | 0.01 | 2.07 |  | 0.00938 | 0.312 | 1e-05 | 5 |
| linear-77x39 | 3120 | Elmer UMFPACK | 0.02 | 0.01 | 2.1 |  | 0.00938 | 0.312 | 0 | 5 |
| linear-77x39 | 3120 | Elmer MUMPS | 0.02 | 0.01 | 2.07 |  | 0.00938 | 0.312 | 0 | 5 |
| quadratic-10x5 | 231 | FEAScript frontal | 0.338 | 0.332 | 2.16 | 0.315 | 0.0667 | 0.8 | 4.99e-06 | 5 |
| quadratic-10x5 | 231 | FEAScript sparse LU | 0.0863 | 0.0586 | 1.91 | 0.0602 | 0.0667 | 0.8 | 4.99e-06 | 5 |
| quadratic-10x5 | 231 | Elmer BiCGStab+ILU0 | 0 | 0 | 2.05 |  | 0.0667 | 0.8 | 1e-05 | 5 |
| quadratic-10x5 | 231 | Elmer UMFPACK | 0 | 0 | 2.05 |  | 0.0667 | 0.8 | 0 | 5 |
| quadratic-10x5 | 231 | Elmer MUMPS | 0 | 0 | 2.06 |  | 0.0667 | 0.8 | 0 | 5 |
| quadratic-20x10 | 861 | FEAScript frontal | 0.921 | 0.905 | 3.08 | 1.02 | 0.0169 | 0.394 | 4.99e-06 | 5 |
| quadratic-20x10 | 861 | FEAScript sparse LU | 0.257 | 0.189 | 2.25 | 0.188 | 0.0169 | 0.394 | 4.99e-06 | 5 |
| quadratic-20x10 | 861 | Elmer BiCGStab+ILU0 | 0.01 | 0 | 2.04 |  | 0.0169 | 0.394 | 1e-06 | 5 |
| quadratic-20x10 | 861 | Elmer UMFPACK | 0.01 | 0 | 2.04 |  | 0.0169 | 0.394 | 0 | 5 |
| quadratic-20x10 | 861 | Elmer MUMPS | 0.01 | 0 | 2.04 |  | 0.0169 | 0.394 | 0 | 5 |
| quadratic-40x20 | 3321 | FEAScript frontal | 27.8 | 27.6 | 119 | 25.2 | 0.00426 | 0.196 | 5e-06 | 1 |
| quadratic-40x20 | 3321 | FEAScript sparse LU | 1.23 | 0.804 | 3.09 | 1.18 | 0.00426 | 0.196 | 5e-06 | 5 |
| quadratic-40x20 | 3321 | Elmer BiCGStab+ILU0 | 0.02 | 0.02 | 2.08 |  | 0.00426 | 0.196 | 1e-05 | 5 |
| quadratic-40x20 | 3321 | Elmer UMFPACK | 0.02 | 0.01 | 2.08 |  | 0.00426 | 0.196 | 0 | 5 |
| quadratic-40x20 | 3321 | Elmer MUMPS | 0.02 | 0.01 | 2.08 |  | 0.00426 | 0.196 | 0 | 5 |
| quadratic-80x40 |  | FEAScript frontal | out of memory |  |  |  |  |  |  |  |
| quadratic-80x40 | 13041 | FEAScript sparse LU | 43.5 | 35.9 | 172 | 41.9 | 0.00107 | 0.0975 | 5e-06 | 1 |
| quadratic-80x40 | 13041 | Elmer BiCGStab+ILU0 | 0.15 | 0.12 | 2.31 |  | 0.00107 | 0.0975 | 1e-05 | 5 |
| quadratic-80x40 | 13041 | Elmer UMFPACK | 0.1 | 0.06 | 2.25 |  | 0.00107 | 0.0975 | 0 | 5 |
| quadratic-80x40 | 13041 | Elmer MUMPS | 0.12 | 0.09 | 2.3 |  | 0.00107 | 0.0975 | 0 | 5 |
| quadratic-160x80 |  | FEAScript frontal | out of memory |  |  |  |  |  |  |  |
| quadratic-160x80 |  | FEAScript sparse LU | out of memory |  |  |  |  |  |  |  |
| quadratic-160x80 | 51681 | Elmer BiCGStab+ILU0 | 1.19 | 1.06 | 3.71 |  | 0.000268 | 0.0487 | 1e-05 | 5 |
| quadratic-160x80 | 51681 | Elmer UMFPACK | 0.63 | 0.5 | 3.16 |  | 0.000268 | 0.0487 | 0 | 5 |
| quadratic-160x80 | 51681 | Elmer MUMPS | 0.5 | 0.37 | 3.01 |  | 0.000268 | 0.0487 | 1e-06 | 5 |
