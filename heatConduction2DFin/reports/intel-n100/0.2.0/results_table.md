| case | nodes | code | solve | linsolve | process | warmWall | peakMemoryMB | rmsErr | maxErr | maxDiffVsElmerUMFPACK | maxDiffVsFEAScript | nruns |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| linear-20x10 | 231 | FEAScript frontal | 0.232 | 0.223 | 2.21 | 0.29 | 156 | 0.646 | 6.07 | 5.08 |  | 5 |
| linear-20x10 | 231 | FEAScript sparse LU | 0.0953 | 0.0754 | 2.73 | 0.0546 | 122 | 0.646 | 6.07 | 5.08 |  | 5 |
| linear-20x10 | 231 | FEAScript Jacobi | 0.143 | 0.127 | 2.71 | 0.134 | 123 | 0.646 | 6.07 | 5.08 |  | 5 |
| linear-20x10 | 231 | scikit-fem SuperLU | 0.013 | 0.002 | 0.46 |  | 60.1 | 0.113 | 1.02 | 4.96e-06 | 5.08 | 5 |
| linear-20x10 | 231 | Elmer BiCGStab+ILU0 | 0 | 0 | 2.07 |  | 30.4 | 0.113 | 1.02 | 1e-06 |  | 5 |
| linear-20x10 | 231 | Elmer UMFPACK | 0 | 0 | 2.09 |  | 30.7 | 0.113 | 1.02 | 0 |  | 5 |
| linear-20x10 | 231 | Elmer MUMPS | 0 | 0 | 2.08 |  | 32.6 | 0.113 | 1.02 | 0 |  | 5 |
| linear-40x20 | 861 | FEAScript frontal | 0.388 | 0.364 | 3.13 | 0.466 | 166 | 0.186 | 3.08 | 2.66 |  | 5 |
| linear-40x20 | 861 | FEAScript sparse LU | 0.295 | 0.206 | 2.93 | 0.26 | 138 | 0.186 | 3.08 | 2.66 |  | 5 |
| linear-40x20 | 861 | FEAScript Jacobi | 4.86 | 4.81 | 6.91 | 5.38 | 135 | 0.186 | 3.08 | 2.66 |  | 5 |
| linear-40x20 | 861 | scikit-fem SuperLU | 0.0145 | 0.00366 | 0.359 |  | 61.1 | 0.0316 | 0.574 | 4.99e-06 | 2.66 | 5 |
| linear-40x20 | 861 | Elmer BiCGStab+ILU0 | 0.01 | 0 | 2.05 |  | 30.9 | 0.0316 | 0.574 | 1e-05 |  | 5 |
| linear-40x20 | 861 | Elmer UMFPACK | 0.01 | 0 | 2.06 |  | 31.5 | 0.0316 | 0.574 | 0 |  | 5 |
| linear-40x20 | 861 | Elmer MUMPS | 0.01 | 0 | 2.07 |  | 33.7 | 0.0316 | 0.574 | 0 |  | 5 |
| linear-80x40 | 3321 | FEAScript frontal | 1.19 | 0.927 | 3.57 | 1.35 | 354 | 0.0515 | 1.55 | 1.36 |  | 5 |
| linear-80x40 | 3321 | FEAScript sparse LU | 1.52 | 1.02 | 3.57 | 1.26 | 307 | 0.0515 | 1.55 | 1.36 |  | 5 |
| linear-80x40 | 3321 | FEAScript Jacobi | 251 | 251 | 254 |  | 319 | 0.0515 | 1.55 | 1.36 |  | 1 |
| linear-80x40 | 3321 | scikit-fem SuperLU | 0.0371 | 0.0148 | 0.351 |  | 66.7 | 0.00883 | 0.307 | 5e-06 | 1.36 | 5 |
| linear-80x40 | 3321 | Elmer BiCGStab+ILU0 | 0.03 | 0.01 | 2.06 |  | 33.5 | 0.00883 | 0.307 | 1e-05 |  | 5 |
| linear-80x40 | 3321 | Elmer UMFPACK | 0.02 | 0.01 | 2.06 |  | 35.6 | 0.00883 | 0.307 | 0 |  | 5 |
| linear-80x40 | 3321 | Elmer MUMPS | 0.02 | 0.01 | 2.06 |  | 38.2 | 0.00883 | 0.307 | 0 |  | 5 |
| linear-160x80 |  | FEAScript frontal | out of memory |  |  |  |  |  |  |  |  |  |
| linear-160x80 | 13041 | FEAScript sparse LU | 40.9 | 33.5 | 43.1 |  | 1.83e+03 | 0.0139 | 0.774 | 0.691 |  | 1 |
| linear-160x80 |  | FEAScript Jacobi | timeout (> 600 s) |  |  |  |  |  |  |  |  |  |
| linear-160x80 | 13041 | scikit-fem SuperLU | 0.141 | 0.0745 | 0.459 |  | 93.9 | 0.00244 | 0.159 | 5e-06 | 0.691 | 5 |
| linear-160x80 | 13041 | Elmer BiCGStab+ILU0 | 0.15 | 0.1 | 2.22 |  | 41.5 | 0.00244 | 0.159 | 1e-05 |  | 5 |
| linear-160x80 | 13041 | Elmer UMFPACK | 0.09 | 0.05 | 2.16 |  | 51.6 | 0.00244 | 0.159 | 0 |  | 5 |
| linear-160x80 | 13041 | Elmer MUMPS | 0.11 | 0.07 | 2.18 |  | 55.6 | 0.00244 | 0.159 | 0 |  | 5 |
| linear-320x160 |  | FEAScript frontal | out of memory |  |  |  |  |  |  |  |  |  |
| linear-320x160 |  | FEAScript sparse LU | out of memory |  |  |  |  |  |  |  |  |  |
| linear-320x160 |  | FEAScript Jacobi | out of memory |  |  |  |  |  |  |  |  |  |
| linear-320x160 | 51681 | scikit-fem SuperLU | 0.726 | 0.444 | 1.04 |  | 210 | 0.000666 | 0.0812 | 5e-06 |  | 5 |
| linear-320x160 | 51681 | Elmer BiCGStab+ILU0 | 1.02 | 0.84 | 3.19 |  | 75.6 | 0.000666 | 0.0812 | 3e-05 |  | 5 |
| linear-320x160 | 51681 | Elmer UMFPACK | 0.48 | 0.3 | 2.66 |  | 122 | 0.000666 | 0.0812 | 0 |  | 5 |
| linear-320x160 | 51681 | Elmer MUMPS | 0.48 | 0.3 | 2.66 |  | 133 | 0.000666 | 0.0812 | 0 |  | 5 |
| linear-77x39 | 3120 | FEAScript frontal | 0.883 | 0.638 | 2.75 | 0.884 | 341 | 0.0548 | 1.61 | 1.41 |  | 5 |
| linear-77x39 | 3120 | FEAScript sparse LU | 1.1 | 0.715 | 2.98 | 1.11 | 351 | 0.0548 | 1.61 | 1.41 |  | 5 |
| linear-77x39 |  | FEAScript Jacobi | not converged |  |  |  |  |  |  |  |  |  |
| linear-77x39 | 3120 | scikit-fem SuperLU | 0.0351 | 0.0137 | 0.347 |  | 66.4 | 0.00938 | 0.312 | 5e-06 | 1.41 | 5 |
| linear-77x39 | 3120 | Elmer BiCGStab+ILU0 | 0.02 | 0.01 | 2.06 |  | 32.9 | 0.00938 | 0.312 | 1e-05 |  | 5 |
| linear-77x39 | 3120 | Elmer UMFPACK | 0.02 | 0.01 | 2.06 |  | 35.2 | 0.00938 | 0.312 | 0 |  | 5 |
| linear-77x39 | 3120 | Elmer MUMPS | 0.02 | 0.01 | 2.06 |  | 37.5 | 0.00938 | 0.312 | 0 |  | 5 |
| quadratic-10x5 | 231 | FEAScript frontal | 0.338 | 0.331 | 2.21 | 0.317 | 164 | 0.0667 | 0.8 | 4.99e-06 |  | 5 |
| quadratic-10x5 | 231 | FEAScript sparse LU | 0.0901 | 0.0622 | 1.94 | 0.0644 | 123 | 0.0667 | 0.8 | 4.99e-06 |  | 5 |
| quadratic-10x5 | 231 | FEAScript Jacobi | 0.144 | 0.108 | 1.99 | 0.125 | 124 | 0.0668 | 0.799 | 0.00666 |  | 5 |
| quadratic-10x5 | 231 | scikit-fem SuperLU | 0.012 | 0.0012 | 0.332 |  | 60.2 | 0.0667 | 0.8 | 4.99e-06 | 5.68e-13 | 5 |
| quadratic-10x5 | 231 | Elmer BiCGStab+ILU0 | 0 | 0 | 2.03 |  | 30.6 | 0.0667 | 0.8 | 1e-05 |  | 5 |
| quadratic-10x5 | 231 | Elmer UMFPACK | 0 | 0 | 2.03 |  | 31 | 0.0667 | 0.8 | 0 |  | 5 |
| quadratic-10x5 | 231 | Elmer MUMPS | 0 | 0 | 2.04 |  | 32.8 | 0.0667 | 0.8 | 0 |  | 5 |
| quadratic-20x10 | 861 | FEAScript frontal | 0.862 | 0.848 | 2.7 | 0.974 | 194 | 0.0169 | 0.394 | 4.99e-06 |  | 5 |
| quadratic-20x10 | 861 | FEAScript sparse LU | 0.257 | 0.188 | 2.09 | 0.193 | 143 | 0.0169 | 0.394 | 4.99e-06 |  | 5 |
| quadratic-20x10 | 861 | FEAScript Jacobi | 4.65 | 4.58 | 6.46 | 5.11 | 138 | 0.0225 | 0.393 | 0.0272 |  | 5 |
| quadratic-20x10 | 861 | scikit-fem SuperLU | 0.0157 | 0.00307 | 0.327 |  | 61.1 | 0.0169 | 0.394 | 4.99e-06 | 1.31e-12 | 5 |
| quadratic-20x10 | 861 | Elmer BiCGStab+ILU0 | 0 | 0 | 2.05 |  | 31.5 | 0.0169 | 0.394 | 1e-06 |  | 5 |
| quadratic-20x10 | 861 | Elmer UMFPACK | 0 | 0 | 2.04 |  | 32.1 | 0.0169 | 0.394 | 0 |  | 5 |
| quadratic-20x10 | 861 | Elmer MUMPS | 0.01 | 0 | 2.04 |  | 34 | 0.0169 | 0.394 | 0 |  | 5 |
| quadratic-40x20 | 3321 | FEAScript frontal | 27.8 | 27.5 | 29.9 |  | 850 | 0.00426 | 0.196 | 5e-06 |  | 1 |
| quadratic-40x20 | 3321 | FEAScript sparse LU | 1.22 | 0.797 | 3.08 | 1.3 | 366 | 0.00426 | 0.196 | 5e-06 |  | 5 |
| quadratic-40x20 | 3321 | FEAScript Jacobi | 227 | 227 | 229 |  | 359 | 0.06 | 0.192 | 0.109 |  | 1 |
| quadratic-40x20 | 3321 | scikit-fem SuperLU | 0.036 | 0.0157 | 0.349 |  | 67 | 0.00426 | 0.196 | 5e-06 | 4.46e-12 | 5 |
| quadratic-40x20 | 3321 | Elmer BiCGStab+ILU0 | 0.02 | 0.02 | 2.08 |  | 33.4 | 0.00426 | 0.196 | 1e-05 |  | 5 |
| quadratic-40x20 | 3321 | Elmer UMFPACK | 0.02 | 0.01 | 2.08 |  | 36 | 0.00426 | 0.196 | 0 |  | 5 |
| quadratic-40x20 | 3321 | Elmer MUMPS | 0.02 | 0.01 | 2.08 |  | 38.2 | 0.00426 | 0.196 | 0 |  | 5 |
| quadratic-80x40 |  | FEAScript frontal | out of memory |  |  |  |  |  |  |  |  |  |
| quadratic-80x40 | 13041 | FEAScript sparse LU | 41 | 33.6 | 43.2 |  | 1.83e+03 | 0.00107 | 0.0975 | 5e-06 |  | 1 |
| quadratic-80x40 |  | FEAScript Jacobi | timeout (> 600 s) |  |  |  |  |  |  |  |  |  |
| quadratic-80x40 | 13041 | scikit-fem SuperLU | 0.169 | 0.11 | 0.484 |  | 97.4 | 0.00107 | 0.0975 | 5e-06 | 1.55e-11 | 5 |
| quadratic-80x40 | 13041 | Elmer BiCGStab+ILU0 | 0.16 | 0.12 | 2.31 |  | 41 | 0.00107 | 0.0975 | 1e-05 |  | 5 |
| quadratic-80x40 | 13041 | Elmer UMFPACK | 0.09 | 0.06 | 2.24 |  | 54.1 | 0.00107 | 0.0975 | 0 |  | 5 |
| quadratic-80x40 | 13041 | Elmer MUMPS | 0.12 | 0.08 | 2.26 |  | 57.8 | 0.00107 | 0.0975 | 0 |  | 5 |
| quadratic-160x80 |  | FEAScript frontal | out of memory |  |  |  |  |  |  |  |  |  |
| quadratic-160x80 |  | FEAScript sparse LU | out of memory |  |  |  |  |  |  |  |  |  |
| quadratic-160x80 |  | FEAScript Jacobi | out of memory |  |  |  |  |  |  |  |  |  |
| quadratic-160x80 | 51681 | scikit-fem SuperLU | 1.24 | 1.03 | 1.56 |  | 257 | 0.000268 | 0.0487 | 5e-06 |  | 5 |
| quadratic-160x80 | 51681 | Elmer BiCGStab+ILU0 | 1.18 | 1.05 | 3.71 |  | 72.6 | 0.000268 | 0.0487 | 1e-05 |  | 5 |
| quadratic-160x80 | 51681 | Elmer UMFPACK | 0.63 | 0.5 | 3.16 |  | 142 | 0.000268 | 0.0487 | 0 |  | 5 |
| quadratic-160x80 | 51681 | Elmer MUMPS | 0.5 | 0.37 | 3.02 |  | 132 | 0.000268 | 0.0487 | 1e-06 |  | 5 |
