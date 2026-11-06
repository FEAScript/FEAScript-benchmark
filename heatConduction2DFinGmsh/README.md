<img src="https://feascript.github.io/FEAScript-website/assets/feascript-logo.png" width="80" alt="FEAScript Logo">

# FEAScript vs Elmer and scikit-fem benchmark: 2D fin on Gmsh meshes

This folder compares [FEAScript](https://feascript.com/) with the [Elmer](https://www.elmerfem.org/) finite element solver and the [scikit-fem](https://github.com/kinnala/scikit-fem) finite element library on unstructured meshes made with [Gmsh](https://gmsh.info/). The problem is the 2D fin of [heatConduction2DFin](../heatConduction2DFin/), which has an exact solution. All the codes read the same meshes, so this tests what structured meshes do not: reading a mesh file, triangles, distorted quadrilaterals, and elements with no regular numbering.

## Contents

- [Results](#results)
- [The problem](#the-problem)
- [What is measured](#what-is-measured)
- [How to run the benchmark](#how-to-run-the-benchmark)
- [License](#license)

## Results

The report of each run is in `reports/<machine>/<FEAScript version>/`. The results of each code are in `<code>/results/<machine>/<its version>/`, and those of FEAScript also by runtime, in `feascript/results/<machine>/<FEAScript version>/<runtime>/<its version>/`:

| Machine | FEAScript version | Results |
|---|---|---|
| Intel N100 | 0.3.1 | [reports/intel-n100/0.3.1/](reports/intel-n100/0.3.1/) |
| Intel N100 | 0.4.0-rc | [reports/intel-n100/0.4.0-rc/](reports/intel-n100/0.4.0-rc/) |

Each report has a README with the plots of that run, a table of all the numbers (`results_table.md`) and the details of the run (`meta.json`): the versions of all the software, the machine and the date.

> **About the comparison:** Elmer runs here on one core, as a single MPI process, on small 2D problems, so that the codes are compared on the same terms. See [About the comparison](../README.md#about-the-comparison).

## The problem

- **Domain:** 4 × 2 rectangle, thermal conductivity k = 1
- **Constant temperature:** T = 200 at the bottom and right edges
- **Symmetry:** zero heat flux on the left edge
- **Convection:** h = 1 and T∞ = 20 on the top edge
- **Exact solution:** the Fourier series of [heatConduction2DFin](../heatConduction2DFin/README.md#the-problem), evaluated to better than 1e-6

## What is measured

`gmsh/fin.geo` describes the geometry, and the benchmark runs Gmsh on it for each mesh:

- **Triangles:** linear (3-node) and quadratic (6-node), with target element sizes 0.2, 0.1, 0.05 and 0.025
- **Quadrilaterals:** linear (4-node) and quadratic (9-node), with target element sizes 0.4, 0.2, 0.1 and 0.05. Gmsh splits every triangle into three quadrilaterals, which halves the element size and gives distorted elements

On each mesh, the benchmark runs:

- **FEAScript:** the `frontal` and `lusolve` direct solvers, reading the `.msh` file with `importGmshMesh`
- **Elmer:** the UMFPACK direct solver, on the mesh converted with ElmerGrid
- **scikit-fem:** its default direct solver (SuperLU from SciPy), reading the `.msh` file with [meshio](https://github.com/nschloe/meshio), once with the Gauss rules of FEAScript and once with a much finer rule

FEAScript also runs in Chromium and Firefox on the three finest quadratic meshes of each shape, with `frontal` and `lusolve`: see [Browsers](../README.md#browsers).

The compared quantities are the RMS and largest error against the exact solution, the largest difference from FEAScript at the same nodes, the assembly and solve time, the end-to-end time and the peak memory, measured as in [heatConduction2DFin](../heatConduction2DFin/README.md#what-is-measured). Reading the mesh is part of the end-to-end time, not of the assembly and solve time.

On a triangle with straight sides, the Jacobian is constant, so Gauss quadrature integrates the stiffness matrix exactly. On a distorted quadrilateral it does not: the integrand is no longer a polynomial, and the result depends on the rule. FEAScript uses 2 × 2 points on linear quadrilaterals and 3 × 3 on quadratic ones, which is why the main scikit-fem run uses the same rules, and the run with a finer rule shows what they cost in accuracy.

## How to run the benchmark

The benchmark needs what [heatConduction2DFin](../heatConduction2DFin/README.md#how-to-run-the-benchmark) needs, plus Gmsh on the `PATH` and the Python package meshio:

```
~/.venvs/feascript-benchmark/bin/pip install meshio
~/.venvs/feascript-benchmark/bin/python benchmark.py   # writes <code>/results/ and reports/
python3 make_report.py <machine> <version>             # writes the plots, results_table.md and README.md
```

It takes the same environment variables as [heatConduction2DFin](../heatConduction2DFin/README.md#how-to-run-the-benchmark). `ONLY` runs some meshes, e.g. `ONLY=tri-linear-h0.2`, and `NO_BROWSERS=1` and `ONLY_BROWSERS=1` leave out or run only the browsers.

The files in this folder:

- **`benchmark.py`:** generates the meshes, runs all the codes, compares them and writes the results
- **`make_report.py`:** draws the plots and writes the results table and README of a run
- **`gmsh/fin.geo`:** the geometry and mesh settings
- **`feascript/run_feascript.mjs`:** runs one FEAScript case
- **`elmer/case.sif.in`:** the Elmer input template
- **`scikit-fem/run_skfem.py`:** runs one scikit-fem case
- **`gmsh/meshes/` and `elmer/meshes/`:** the meshes, generated by the benchmark and not committed
- **`feascript/case.mjs`:** the FEAScript model, shared by Node.js and the browsers
- **`feascript/results/<machine>/<FEAScript version>/<runtime>/<its version>/`:** the results of FEAScript in Node.js, Chromium and Firefox: `results.json`, and in Node.js nodal results (not committed)
- **`elmer/results/<machine>/<its version>/` and `scikit-fem/results/<machine>/<its version>/`:** the latest results of Elmer and scikit-fem: `results.json`, nodal results (not committed) and the Elmer `.sif` file
- **`reports/<machine>/<FEAScript version>/`:** the report of one run: README, plots, results table, `meta.json`, `results.json` and `browsers.json`

## License

This benchmark is released under the [MIT license](../LICENSE). Note that the core library of FEAScript is distributed under the terms of the [MIT license](https://github.com/FEAScript/FEAScript-core/blob/main/LICENSE).
