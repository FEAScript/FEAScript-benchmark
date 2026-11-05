#!/usr/bin/env python3
# ════════════════════════════════════════════════════════════════
#  FEAScript Benchmark
#  Finite Element Simulation in JavaScript
#  https://github.com/FEAScript/FEAScript-benchmark
#  MIT License © 2026 FEAScript
# ════════════════════════════════════════════════════════════════

"""Run one scikit-fem case: python3 run_skfem.py <mesh.msh> <fine|matched> <outCsv|->

Solves the fin on a Gmsh mesh with scikit-fem's default direct solver (SciPy's SuperLU). The "matched" integration
uses the Gauss rules of FEAScript (2 x 2 on linear quadrilaterals, 3 x 3 on quadratic ones), and "fine" a much higher
order. Both are exact on triangles, where the Jacobian is constant, so only quadrilaterals differ.
"""
import json, sys, time
import meshio
import numpy as np
from skfem import Basis, BilinearForm, ElementQuad1, ElementQuad2, ElementTriP1, ElementTriP2, FacetBasis, LinearForm, MeshQuad, MeshTri, condense, solve
from skfem.helpers import dot, grad

mesh_file, integration, out_csv = sys.argv[1:4]
H, T_INF, T_FIXED = 1.0, 20.0, 200.0  # k = 1


@BilinearForm
def conduction(u, v, _):
    return dot(grad(u), grad(v))


@BilinearForm
def convection(u, v, _):
    return H * u * v


@LinearForm
def convection_load(v, _):
    return H * T_INF * v


# Read the mesh: only the vertices are needed, since scikit-fem places the higher-order nodes where Gmsh does
raw = meshio.read(mesh_file)
shape = "quad" if any(c.type.startswith("quad") for c in raw.cells) else "triangle"
cells = np.vstack([c.data for c in raw.cells if c.type.startswith(shape)])
order = 1 if cells.shape[1] in (3, 4) else 2
vertices = cells[:, : 3 if shape == "triangle" else 4]
used, numbering = np.unique(vertices, return_inverse=True)
vertices = numbering.reshape(vertices.shape).T
points = raw.points[used, :2].T

# Timed like FEAScript's model.solve(): assembly and linear solve (reading the mesh is not included)
t0 = time.perf_counter()
mesh = (MeshTri if shape == "triangle" else MeshQuad)(points, vertices, sort_t=False).with_boundaries({
    "fixed": lambda x: np.isclose(x[1], 0) | np.isclose(x[0], 4),
    "top": lambda x: np.isclose(x[1], 2),
})  # The left edge is the symmetry boundary: zero flux, the natural condition
element = {("triangle", 1): ElementTriP1, ("triangle", 2): ElementTriP2, ("quad", 1): ElementQuad1, ("quad", 2): ElementQuad2}[(shape, order)]()
# A Gauss rule with n x n points on a quadrilateral has intorder 2n - 1 (and intorder 2n - 2 selects the same rule)
intorder = {"matched": 2 * order if shape == "triangle" else 2 * (order + 1) - 1, "fine": 12}[integration]
interior = Basis(mesh, element, intorder=intorder)
top = FacetBasis(mesh, element, facets=mesh.boundaries["top"], intorder=2 * order + 1)
A = conduction.assemble(interior) + convection.assemble(top)
b = convection_load.assemble(top)
fixed = interior.get_dofs("fixed").all()
T = interior.zeros()
T[fixed] = T_FIXED
t1 = time.perf_counter()
T = solve(*condense(A, b, x=T, D=fixed))
t2 = time.perf_counter()

if out_csv != "-":
    x, y = interior.doflocs
    np.savetxt(out_csv, np.column_stack([x, y, T]), delimiter=",", header="x,y,T", comments="", fmt="%.17g")
print(json.dumps({"nodes": len(T), "wall": t2 - t0, "linsolve": t2 - t1}))
