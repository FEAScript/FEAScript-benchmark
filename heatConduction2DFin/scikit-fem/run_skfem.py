#!/usr/bin/env python3
# ════════════════════════════════════════════════════════════════
#  FEAScript Benchmark
#  Finite Element Simulation in JavaScript
#  https://github.com/FEAScript/FEAScript-benchmark
#  MIT License © 2026 FEAScript
# ════════════════════════════════════════════════════════════════

"""Run one scikit-fem case: python3 run_skfem.py <nx> <ny> <order> <outCsv|->

Solves the same 2D fin as run_feascript.mjs on the same structured quadrilateral mesh, with Q1 (4-node) or
Q2 (9-node) elements and scikit-fem's default direct solver (SciPy's SuperLU).
"""
import json, sys, time
import numpy as np
from skfem import Basis, BilinearForm, ElementQuad1, ElementQuad2, FacetBasis, LinearForm, MeshQuad, condense, solve
from skfem.helpers import dot, grad

nx, ny, order, out_csv = int(sys.argv[1]), int(sys.argv[2]), sys.argv[3], sys.argv[4]
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


# Timed like FEAScript's model.solve(): mesh generation, assembly and linear solve
t0 = time.perf_counter()
mesh = MeshQuad.init_tensor(np.linspace(0, 4, nx + 1), np.linspace(0, 2, ny + 1)).with_boundaries({
    "bottom": lambda x: np.isclose(x[1], 0),
    "right": lambda x: np.isclose(x[0], 4),
    "top": lambda x: np.isclose(x[1], 2),
})  # The left edge is the symmetry boundary: zero flux, the natural condition
element, intorder = (ElementQuad1(), 2) if order == "linear" else (ElementQuad2(), 4)
interior = Basis(mesh, element, intorder=intorder)
top = FacetBasis(mesh, element, facets=mesh.boundaries["top"], intorder=intorder)
A = conduction.assemble(interior) + convection.assemble(top)
b = convection_load.assemble(top)
fixed = interior.get_dofs({"bottom", "right"}).all()
T = interior.zeros()
T[fixed] = T_FIXED
t1 = time.perf_counter()
T = solve(*condense(A, b, x=T, D=fixed))
t2 = time.perf_counter()

if out_csv != "-":
    x, y = interior.doflocs
    np.savetxt(out_csv, np.column_stack([x, y, T]), delimiter=",", header="x,y,T", comments="", fmt="%.17g")
print(json.dumps({"nodes": len(T), "wall": t2 - t0, "linsolve": t2 - t1}))
