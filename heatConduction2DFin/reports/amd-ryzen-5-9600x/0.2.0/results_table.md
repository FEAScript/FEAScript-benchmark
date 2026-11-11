| case | nodes | code | solve | linsolve | process | warmWall | peakMemoryMB | rmsErr | maxErr | maxDiffVsElmerUMFPACK | nruns |
|---|---|---|---|---|---|---|---|---|---|---|---|
| linear-20x10 | 231 | FEAScript frontal | 0.0965 | 0.0937 | 0.781 | 0.0958 | 150 | 0.646 | 6.07 | 5.08 | 5 |
| linear-20x10 | 231 | FEAScript sparse LU | 0.0283 | 0.0204 | 0.726 | 0.0114 | 122 | 0.646 | 6.07 | 5.08 | 5 |
| linear-20x10 | 231 | Elmer BiCGStab+ILU0 | 0 | 0 | 0.47 |  | 29.9 | 0.113 | 1.02 | 5.44e-08 | 5 |
| linear-20x10 | 231 | Elmer UMFPACK | 0 | 0 | 0.47 |  | 30 | 0.113 | 1.02 | 0 | 5 |
| linear-20x10 | 231 | Elmer MUMPS | 0 | 0 | 0.47 |  | 31.9 | 0.113 | 1.02 | 2.27e-13 | 5 |
| linear-40x20 | 861 | FEAScript frontal | 0.127 | 0.105 | 0.813 | 0.129 | 165 | 0.186 | 3.08 | 2.66 | 5 |
| linear-40x20 | 861 | FEAScript sparse LU | 0.108 | 0.0853 | 0.785 | 0.0737 | 139 | 0.186 | 3.08 | 2.66 | 5 |
| linear-40x20 | 861 | Elmer BiCGStab+ILU0 | 0 | 0 | 0.471 |  | 30.4 | 0.0316 | 0.574 | 2.42e-07 | 5 |
| linear-40x20 | 861 | Elmer UMFPACK | 0 | 0 | 0.47 |  | 30.9 | 0.0316 | 0.574 | 0 | 5 |
| linear-40x20 | 861 | Elmer MUMPS | 0 | 0 | 0.471 |  | 33.1 | 0.0316 | 0.574 | 7.82e-13 | 5 |
| linear-80x40 | 3321 | FEAScript frontal | 0.358 | 0.254 | 1.03 | 0.285 | 351 | 0.0515 | 1.55 | 1.36 | 5 |
| linear-80x40 | 3321 | FEAScript sparse LU | 0.446 | 0.277 | 1.17 | 0.424 | 362 | 0.0515 | 1.55 | 1.36 | 5 |
| linear-80x40 | 3321 | Elmer BiCGStab+ILU0 | 0.01 | 0.01 | 0.476 |  | 33.1 | 0.00883 | 0.307 | 6.48e-07 | 5 |
| linear-80x40 | 3321 | Elmer UMFPACK | 0.01 | 0 | 0.483 |  | 35.1 | 0.00883 | 0.307 | 0 | 5 |
| linear-80x40 | 3321 | Elmer MUMPS | 0.01 | 0.01 | 0.484 |  | 37.5 | 0.00883 | 0.307 | 2.39e-12 | 5 |
| linear-160x80 |  | FEAScript frontal | out of memory |  |  |  |  |  |  |  |  |
| linear-160x80 | 13041 | FEAScript sparse LU | 6.17 | 3.76 | 6.95 | 6.21 | 1.87e+03 | 0.0139 | 0.774 | 0.691 | 5 |
| linear-160x80 | 13041 | Elmer BiCGStab+ILU0 | 0.06 | 0.04 | 0.526 |  | 41 | 0.00244 | 0.159 | 6.32e-06 | 5 |
| linear-160x80 | 13041 | Elmer UMFPACK | 0.04 | 0.02 | 0.515 |  | 51 | 0.00244 | 0.159 | 0 | 5 |
| linear-160x80 | 13041 | Elmer MUMPS | 0.05 | 0.03 | 0.525 |  | 54.8 | 0.00244 | 0.159 | 1.08e-11 | 5 |
| linear-320x160 |  | FEAScript frontal | out of memory |  |  |  |  |  |  |  |  |
| linear-320x160 |  | FEAScript sparse LU | out of memory |  |  |  |  |  |  |  |  |
| linear-320x160 | 51681 | Elmer BiCGStab+ILU0 | 0.37 | 0.3 | 0.836 |  | 75 | 0.000666 | 0.0812 | 2.1e-05 | 5 |
| linear-320x160 | 51681 | Elmer UMFPACK | 0.21 | 0.13 | 0.714 |  | 121 | 0.000666 | 0.0812 | 0 | 5 |
| linear-320x160 | 51681 | Elmer MUMPS | 0.24 | 0.16 | 0.746 |  | 131 | 0.000666 | 0.0812 | 3.02e-11 | 5 |
| linear-77x39 | 3120 | FEAScript frontal | 0.337 | 0.241 | 1.01 | 0.266 | 330 | 0.0548 | 1.61 | 1.41 | 5 |
| linear-77x39 | 3120 | FEAScript sparse LU | 0.417 | 0.245 | 1.11 | 0.369 | 320 | 0.0548 | 1.61 | 1.41 | 5 |
| linear-77x39 | 3120 | Elmer BiCGStab+ILU0 | 0.01 | 0.01 | 0.483 |  | 32.4 | 0.00938 | 0.312 | 4.4e-07 | 5 |
| linear-77x39 | 3120 | Elmer UMFPACK | 0.01 | 0 | 0.482 |  | 34.7 | 0.00938 | 0.312 | 0 | 5 |
| linear-77x39 | 3120 | Elmer MUMPS | 0.01 | 0 | 0.482 |  | 36.8 | 0.00938 | 0.312 | 1.55e-12 | 5 |
| quadratic-10x5 | 231 | FEAScript frontal | 0.15 | 0.146 | 0.844 | 0.115 | 161 | 0.0667 | 0.8 | 5.4e-13 | 5 |
| quadratic-10x5 | 231 | FEAScript sparse LU | 0.0422 | 0.0249 | 0.761 | 0.03 | 126 | 0.0667 | 0.8 | 7.11e-13 | 5 |
| quadratic-10x5 | 231 | Elmer BiCGStab+ILU0 | 0 | 0 | 0.456 |  | 30.1 | 0.0667 | 0.8 | 1.29e-08 | 5 |
| quadratic-10x5 | 231 | Elmer UMFPACK | 0 | 0 | 0.47 |  | 30.3 | 0.0667 | 0.8 | 0 | 5 |
| quadratic-10x5 | 231 | Elmer MUMPS | 0 | 0 | 0.47 |  | 32.1 | 0.0667 | 0.8 | 5.68e-13 | 5 |
| quadratic-20x10 | 861 | FEAScript frontal | 0.351 | 0.336 | 1.04 | 0.336 | 191 | 0.0169 | 0.394 | 1.51e-12 | 5 |
| quadratic-20x10 | 861 | FEAScript sparse LU | 0.128 | 0.0917 | 0.832 | 0.0825 | 140 | 0.0169 | 0.394 | 2.67e-12 | 5 |
| quadratic-20x10 | 861 | Elmer BiCGStab+ILU0 | 0 | 0 | 0.473 |  | 30.8 | 0.0169 | 0.394 | 3.37e-08 | 5 |
| quadratic-20x10 | 861 | Elmer UMFPACK | 0 | 0 | 0.473 |  | 31.4 | 0.0169 | 0.394 | 0 | 5 |
| quadratic-20x10 | 861 | Elmer MUMPS | 0 | 0 | 0.472 |  | 33.4 | 0.0169 | 0.394 | 1.11e-12 | 5 |
| quadratic-40x20 | 3321 | FEAScript frontal | 12.2 | 12.1 | 12.9 | 12.2 | 934 | 0.00426 | 0.196 | 1e-11 | 5 |
| quadratic-40x20 | 3321 | FEAScript sparse LU | 0.42 | 0.254 | 1.14 | 0.387 | 365 | 0.00426 | 0.196 | 8.5e-12 | 5 |
| quadratic-40x20 | 3321 | Elmer BiCGStab+ILU0 | 0.01 | 0.01 | 0.49 |  | 32.7 | 0.00426 | 0.196 | 6.52e-07 | 5 |
| quadratic-40x20 | 3321 | Elmer UMFPACK | 0.01 | 0.01 | 0.49 |  | 35.2 | 0.00426 | 0.196 | 0 | 5 |
| quadratic-40x20 | 3321 | Elmer MUMPS | 0.01 | 0.01 | 0.492 |  | 37.5 | 0.00426 | 0.196 | 6.48e-12 | 5 |
| quadratic-80x40 |  | FEAScript frontal | out of memory |  |  |  |  |  |  |  |  |
| quadratic-80x40 | 13041 | FEAScript sparse LU | 6.04 | 3.67 | 6.78 | 6.07 | 1.87e+03 | 0.00107 | 0.0975 | 2.84e-11 | 5 |
| quadratic-80x40 | 13041 | Elmer BiCGStab+ILU0 | 0.06 | 0.05 | 0.556 |  | 40.3 | 0.00107 | 0.0975 | 2.64e-06 | 5 |
| quadratic-80x40 | 13041 | Elmer UMFPACK | 0.04 | 0.03 | 0.536 |  | 53.5 | 0.00107 | 0.0975 | 0 | 5 |
| quadratic-80x40 | 13041 | Elmer MUMPS | 0.05 | 0.04 | 0.545 |  | 56.5 | 0.00107 | 0.0975 | 1.31e-11 | 5 |
| quadratic-160x80 |  | FEAScript frontal | out of memory |  |  |  |  |  |  |  |  |
| quadratic-160x80 |  | FEAScript sparse LU | out of memory |  |  |  |  |  |  |  |  |
| quadratic-160x80 | 51681 | Elmer BiCGStab+ILU0 | 0.39 | 0.34 | 0.976 |  | 71.9 | 0.000268 | 0.0487 | 1.87e-05 | 5 |
| quadratic-160x80 | 51681 | Elmer UMFPACK | 0.25 | 0.2 | 0.878 |  | 141 | 0.000268 | 0.0487 | 0 | 5 |
| quadratic-160x80 | 51681 | Elmer MUMPS | 0.24 | 0.19 | 0.877 |  | 130 | 0.000268 | 0.0487 | 8.56e-11 | 5 |
