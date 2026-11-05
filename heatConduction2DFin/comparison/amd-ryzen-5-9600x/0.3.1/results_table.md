| case | nodes | code | solve | linsolve | process | warmWall | peakMemoryMB | rmsErr | maxErr | maxDiffVsElmerUMFPACK | nruns |
|---|---|---|---|---|---|---|---|---|---|---|---|
| linear-20x10 | 231 | FEAScript frontal | 0.101 | 0.0989 | 0.235 | 0.11 | 125 | 0.113 | 1.02 | 4.96e-06 | 5 |
| linear-20x10 | 231 | FEAScript sparse LU | 0.0523 | 0.0461 | 0.191 | 0.0211 | 73.1 | 0.113 | 1.02 | 4.96e-06 | 5 |
| linear-20x10 | 231 | Elmer BiCGStab+ILU0 | 0 | 0 | 0.47 |  | 29.9 | 0.113 | 1.02 | 1e-06 | 5 |
| linear-20x10 | 231 | Elmer UMFPACK | 0 | 0 | 0.471 |  | 30 | 0.113 | 1.02 | 0 | 5 |
| linear-20x10 | 231 | Elmer MUMPS | 0 | 0 | 0.47 |  | 31.9 | 0.113 | 1.02 | 0 | 5 |
| linear-40x20 | 861 | FEAScript frontal | 0.13 | 0.128 | 0.265 | 0.107 | 130 | 0.0316 | 0.574 | 4.99e-06 | 5 |
| linear-40x20 | 861 | FEAScript sparse LU | 0.0896 | 0.074 | 0.223 | 0.0625 | 74.4 | 0.0316 | 0.574 | 4.99e-06 | 5 |
| linear-40x20 | 861 | Elmer BiCGStab+ILU0 | 0 | 0 | 0.471 |  | 30.4 | 0.0316 | 0.574 | 1e-05 | 5 |
| linear-40x20 | 861 | Elmer UMFPACK | 0 | 0 | 0.472 |  | 30.9 | 0.0316 | 0.574 | 0 | 5 |
| linear-40x20 | 861 | Elmer MUMPS | 0 | 0 | 0.474 |  | 33 | 0.0316 | 0.574 | 0 | 5 |
| linear-80x40 | 3321 | FEAScript frontal | 0.292 | 0.282 | 0.428 | 0.268 | 207 | 0.00883 | 0.307 | 5e-06 | 5 |
| linear-80x40 | 3321 | FEAScript sparse LU | 0.182 | 0.163 | 0.312 | 0.207 | 91.3 | 0.00883 | 0.307 | 5e-06 | 5 |
| linear-80x40 | 3321 | Elmer BiCGStab+ILU0 | 0.01 | 0.01 | 0.48 |  | 33.1 | 0.00883 | 0.307 | 1e-05 | 5 |
| linear-80x40 | 3321 | Elmer UMFPACK | 0.01 | 0 | 0.482 |  | 35.2 | 0.00883 | 0.307 | 0 | 5 |
| linear-80x40 | 3321 | Elmer MUMPS | 0.01 | 0.01 | 0.483 |  | 37.6 | 0.00883 | 0.307 | 0 | 5 |
| linear-160x80 | 13041 | FEAScript frontal | 3.13 | 3.08 | 3.31 | 3.37 | 1.66e+03 | 0.00244 | 0.159 | 5e-06 | 5 |
| linear-160x80 | 13041 | FEAScript sparse LU | 0.509 | 0.468 | 0.643 | 0.674 | 145 | 0.00244 | 0.159 | 5e-06 | 5 |
| linear-160x80 | 13041 | Elmer BiCGStab+ILU0 | 0.06 | 0.04 | 0.524 |  | 41 | 0.00244 | 0.159 | 1e-05 | 5 |
| linear-160x80 | 13041 | Elmer UMFPACK | 0.04 | 0.02 | 0.515 |  | 51.1 | 0.00244 | 0.159 | 0 | 5 |
| linear-160x80 | 13041 | Elmer MUMPS | 0.05 | 0.03 | 0.526 |  | 54.8 | 0.00244 | 0.159 | 0 | 5 |
| linear-320x160 |  | FEAScript frontal | out of memory |  |  |  |  |  |  |  |  |
| linear-320x160 | 51681 | FEAScript sparse LU | 2.03 | 1.91 | 2.19 | 3.44 | 368 | 0.000666 | 0.0812 | 5e-06 | 5 |
| linear-320x160 | 51681 | Elmer BiCGStab+ILU0 | 0.37 | 0.3 | 0.878 |  | 75.1 | 0.000666 | 0.0812 | 3e-05 | 5 |
| linear-320x160 | 51681 | Elmer UMFPACK | 0.21 | 0.13 | 0.714 |  | 121 | 0.000666 | 0.0812 | 0 | 5 |
| linear-320x160 | 51681 | Elmer MUMPS | 0.24 | 0.16 | 0.744 |  | 131 | 0.000666 | 0.0812 | 0 | 5 |
| linear-77x39 | 3120 | FEAScript frontal | 0.279 | 0.269 | 0.412 | 0.254 | 198 | 0.00938 | 0.312 | 5e-06 | 5 |
| linear-77x39 | 3120 | FEAScript sparse LU | 0.168 | 0.149 | 0.294 | 0.183 | 88.9 | 0.00938 | 0.312 | 5e-06 | 5 |
| linear-77x39 | 3120 | Elmer BiCGStab+ILU0 | 0.01 | 0.01 | 0.478 |  | 32.5 | 0.00938 | 0.312 | 1e-05 | 5 |
| linear-77x39 | 3120 | Elmer UMFPACK | 0.01 | 0 | 0.483 |  | 34.7 | 0.00938 | 0.312 | 0 | 5 |
| linear-77x39 | 3120 | Elmer MUMPS | 0.01 | 0 | 0.483 |  | 36.8 | 0.00938 | 0.312 | 0 | 5 |
| quadratic-10x5 | 231 | FEAScript frontal | 0.198 | 0.196 | 0.335 | 0.125 | 133 | 0.0667 | 0.8 | 4.99e-06 | 5 |
| quadratic-10x5 | 231 | FEAScript sparse LU | 0.0532 | 0.0458 | 0.191 | 0.0322 | 72.6 | 0.0667 | 0.8 | 4.99e-06 | 5 |
| quadratic-10x5 | 231 | Elmer BiCGStab+ILU0 | 0 | 0 | 0.47 |  | 30 | 0.0667 | 0.8 | 1e-05 | 5 |
| quadratic-10x5 | 231 | Elmer UMFPACK | 0 | 0 | 0.47 |  | 30.2 | 0.0667 | 0.8 | 0 | 5 |
| quadratic-10x5 | 231 | Elmer MUMPS | 0 | 0 | 0.469 |  | 32.1 | 0.0667 | 0.8 | 0 | 5 |
| quadratic-20x10 | 861 | FEAScript frontal | 0.404 | 0.402 | 0.537 | 0.325 | 157 | 0.0169 | 0.394 | 4.99e-06 | 5 |
| quadratic-20x10 | 861 | FEAScript sparse LU | 0.106 | 0.0914 | 0.236 | 0.0674 | 79.3 | 0.0169 | 0.394 | 4.99e-06 | 5 |
| quadratic-20x10 | 861 | Elmer BiCGStab+ILU0 | 0 | 0 | 0.471 |  | 30.7 | 0.0169 | 0.394 | 1e-06 | 5 |
| quadratic-20x10 | 861 | Elmer UMFPACK | 0 | 0 | 0.474 |  | 31.4 | 0.0169 | 0.394 | 0 | 5 |
| quadratic-20x10 | 861 | Elmer MUMPS | 0 | 0 | 0.475 |  | 33.2 | 0.0169 | 0.394 | 0 | 5 |
| quadratic-40x20 | 3321 | FEAScript frontal | 11.2 | 11.2 | 11.3 | 10.6 | 645 | 0.00426 | 0.196 | 5e-06 | 5 |
| quadratic-40x20 | 3321 | FEAScript sparse LU | 0.182 | 0.158 | 0.311 | 0.209 | 93.1 | 0.00426 | 0.196 | 5e-06 | 5 |
| quadratic-40x20 | 3321 | Elmer BiCGStab+ILU0 | 0.01 | 0.01 | 0.492 |  | 32.7 | 0.00426 | 0.196 | 1e-05 | 5 |
| quadratic-40x20 | 3321 | Elmer UMFPACK | 0.01 | 0.01 | 0.492 |  | 35.2 | 0.00426 | 0.196 | 0 | 5 |
| quadratic-40x20 | 3321 | Elmer MUMPS | 0.01 | 0.01 | 0.488 |  | 37.4 | 0.00426 | 0.196 | 0 | 5 |
| quadratic-80x40 |  | FEAScript frontal | out of memory |  |  |  |  |  |  |  |  |
| quadratic-80x40 | 13041 | FEAScript sparse LU | 0.538 | 0.496 | 0.634 | 0.694 | 152 | 0.00107 | 0.0975 | 5e-06 | 5 |
| quadratic-80x40 | 13041 | Elmer BiCGStab+ILU0 | 0.06 | 0.05 | 0.515 |  | 40.5 | 0.00107 | 0.0975 | 1e-05 | 5 |
| quadratic-80x40 | 13041 | Elmer UMFPACK | 0.04 | 0.03 | 0.536 |  | 53.5 | 0.00107 | 0.0975 | 0 | 5 |
| quadratic-80x40 | 13041 | Elmer MUMPS | 0.05 | 0.04 | 0.547 |  | 56.5 | 0.00107 | 0.0975 | 0 | 5 |
| quadratic-160x80 |  | FEAScript frontal | out of memory |  |  |  |  |  |  |  |  |
| quadratic-160x80 | 51681 | FEAScript sparse LU | 2.43 | 2.29 | 2.57 | 4.09 | 435 | 0.000268 | 0.0487 | 5e-06 | 5 |
| quadratic-160x80 | 51681 | Elmer BiCGStab+ILU0 | 0.39 | 0.33 | 1.02 |  | 71.9 | 0.000268 | 0.0487 | 2e-05 | 5 |
| quadratic-160x80 | 51681 | Elmer UMFPACK | 0.25 | 0.19 | 0.878 |  | 141 | 0.000268 | 0.0487 | 0 | 5 |
| quadratic-160x80 | 51681 | Elmer MUMPS | 0.24 | 0.19 | 0.878 |  | 130 | 0.000268 | 0.0487 | 1e-06 | 5 |
