# NOTICE

FEAScript-benchmark
Copyright (c) 2026 FEAScript

The benchmarks run the following third-party software. None of it is included in this repository. The `results/` and `reports/` folders contain numerical results produced by these programs, not their code.

1. **Chromium**
   - License: BSD 3-Clause, with third-party components under their own licenses (https://chromium.googlesource.com/chromium/src/+/main/LICENSE)
   - Source: https://chromium.googlesource.com/chromium/src
   - One of the browsers that run FEAScript; installed separately and run as an external program

2. **Elmer (ElmerSolver and ElmerGrid)**
   - License: GPL 2.0 or later, with parts of the solver library under LGPL 2.1 (https://github.com/ElmerCSC/elmerfem/tree/devel/license_texts), Copyright CSC - IT Center for Science Ltd.
   - Source: https://github.com/ElmerCSC/elmerfem
   - The reference finite element solver; installed separately and run as an external program

3. **Firefox**
   - License: Mozilla Public License 2.0 (https://www.mozilla.org/MPL/2.0/)
   - Source: https://github.com/mozilla-firefox/firefox
   - One of the browsers that run FEAScript; installed separately and run as an external program

4. **Gmsh**
   - License: GPL 2.0 or later (https://gitlab.onelab.info/gmsh/gmsh/-/blob/master/LICENSE.txt)
   - Source: https://gitlab.onelab.info/gmsh/gmsh
   - Generates the unstructured meshes; installed separately and run as an external program

5. **gnuplot**
   - License: gnuplot license (https://sourceforge.net/p/gnuplot/gnuplot-main/ci/master/tree/Copyright)
   - Source: http://www.gnuplot.info
   - Draws the plots

6. **meshio**
   - License: MIT (https://github.com/nschloe/meshio/blob/main/LICENSE.txt)
   - Source: https://github.com/nschloe/meshio
   - Reads the Gmsh meshes for scikit-fem

7. **Node.js**
   - License: MIT (https://github.com/nodejs/node/blob/main/LICENSE)
   - Source: https://github.com/nodejs/node
   - Runs FEAScript

8. **NumPy**
   - License: BSD 3-Clause (https://github.com/numpy/numpy/blob/main/LICENSE.txt)
   - Source: https://github.com/numpy/numpy
   - Used by the Python scripts for the exact solution and the comparisons

9. **scikit-fem**
   - License: BSD 3-Clause (https://github.com/kinnala/scikit-fem/blob/master/LICENSE), Copyright scikit-fem developers
   - Source: https://github.com/kinnala/scikit-fem
   - A second reference finite element library; installed separately and run as an external program

10. **SciPy**
    - License: BSD 3-Clause (https://github.com/scipy/scipy/blob/main/LICENSE.txt)
    - Source: https://github.com/scipy/scipy
    - Sparse matrices and the SuperLU direct solver used by scikit-fem
