# NOTICE

FEAScript-benchmark
Copyright (c) 2026 FEAScript

The benchmarks run the following third-party software. None of it is included in this repository. The `results/` folders contain numerical results produced by these programs, not their code.

1. **Elmer (ElmerSolver and ElmerGrid)**
   - License: GPL 2.0 or later, with parts of the solver library under LGPL 2.1 (https://github.com/ElmerCSC/elmerfem/tree/devel/license_texts), Copyright CSC - IT Center for Science Ltd.
   - Source: https://github.com/ElmerCSC/elmerfem
   - The reference finite element solver; installed separately and run as an external program

2. **FEAScript**
   - License: MIT (https://github.com/FEAScript/FEAScript-core/blob/main/LICENSE)
   - Source: https://github.com/FEAScript/FEAScript-core
   - The library being benchmarked; loaded from a separate FEAScript-core checkout. Its own third-party notices are in https://github.com/FEAScript/FEAScript-core/blob/main/NOTICE.md

3. **Node.js**
   - License: MIT (https://github.com/nodejs/node/blob/main/LICENSE)
   - Source: https://github.com/nodejs/node
   - Runs FEAScript

4. **NumPy**
   - License: BSD 3-Clause (https://github.com/numpy/numpy/blob/main/LICENSE.txt)
   - Source: https://github.com/numpy/numpy
   - Used by the Python scripts for the exact solution and the comparisons

5. **gnuplot**
   - License: gnuplot license (https://sourceforge.net/p/gnuplot/gnuplot-main/ci/master/tree/Copyright)
   - Source: http://www.gnuplot.info
   - Draws the plots

6. **scikit-fem**
   - License: BSD 3-Clause (https://github.com/kinnala/scikit-fem/blob/master/LICENSE), Copyright scikit-fem developers
   - Source: https://github.com/kinnala/scikit-fem
   - A second reference finite element library; installed separately and run as an external program

7. **SciPy**
   - License: BSD 3-Clause (https://github.com/scipy/scipy/blob/main/LICENSE.txt)
   - Source: https://github.com/scipy/scipy
   - Sparse matrices and the SuperLU direct solver used by scikit-fem
