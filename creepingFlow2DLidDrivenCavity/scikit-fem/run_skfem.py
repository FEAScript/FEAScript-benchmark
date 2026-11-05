#!/usr/bin/env python3
# ════════════════════════════════════════════════════════════════
#  FEAScript Benchmark
#  Finite Element Simulation in JavaScript
#  https://github.com/FEAScript/FEAScript-benchmark
#  MIT License © 2026 FEAScript
# ════════════════════════════════════════════════════════════════

"""Run one scikit-fem case: python3 run_skfem.py <n> <outCsv|->

Solves the same lid-driven cavity as run_feascript.mjs on the same n x n mesh, with Taylor-Hood Q2-Q1 elements and
scikit-fem's default direct solver (SciPy's SuperLU). Like FEAScript, it sets the full lid velocity at every lid
node except the two corners, where the walls win.
"""
import json, sys, time
import numpy as np
from scipy.sparse import bmat
from skfem import Basis, BilinearForm, ElementQuad1, ElementQuad2, ElementVector, MeshQuad, condense, solve
from skfem.helpers import ddot, div, grad

n, out_csv = int(sys.argv[1]), sys.argv[2]
VISCOSITY = 1.0
LID_VELOCITY = 1.0


@BilinearForm
def viscous(u, v, _):
    return VISCOSITY * ddot(grad(u), grad(v))


@BilinearForm
def divergence(p, v, _):
    return -div(v) * p


# Timed like FEAScript's model.solve(): mesh generation, assembly and linear solve
t0 = time.perf_counter()
edges = np.linspace(0, 1, n + 1)
mesh = MeshQuad.init_tensor(edges, edges).with_boundaries({
    "lid": lambda x: np.isclose(x[1], 1),
    "walls": lambda x: np.isclose(x[1], 0) | np.isclose(x[0], 0) | np.isclose(x[0], 1),
})
velocity = Basis(mesh, ElementVector(ElementQuad2()), intorder=4)
pressure = velocity.with_element(ElementQuad1())
A = viscous.assemble(velocity)
B = divergence.assemble(pressure, velocity)
K = bmat([[A, B], [B.T, None]], format="csr")
b = np.zeros(K.shape[0])

# Velocity on the lid and walls (the walls win at the two lid corners), and pressure 0 at (0, 0)
lid, walls = velocity.get_dofs("lid"), velocity.get_dofs("walls")
pressure_dof = velocity.N + int(np.argmin(np.sum(pressure.doflocs ** 2, axis=0)))
x = np.zeros(K.shape[0])
x[lid.all("u^1")] = LID_VELOCITY
x[walls.all()] = 0.0
fixed = np.concatenate([lid.all(), walls.all(), [pressure_dof]])
t1 = time.perf_counter()
x = solve(*condense(K, b, x=x, D=np.unique(fixed)))
t2 = time.perf_counter()

if out_csv != "-":
    # The dofs of each velocity component follow the same node order
    X, Y = velocity.doflocs[:, 0::2]
    u, v = x[: velocity.N : 2], x[1 : velocity.N : 2]
    p = np.full(len(X), np.nan)  # Q1 pressure: known at the mesh vertices only
    is_vertex = np.isclose(X * n, np.round(X * n)) & np.isclose(Y * n, np.round(Y * n))
    vertex_p = dict(zip(zip(np.round(pressure.doflocs[0], 7), np.round(pressure.doflocs[1], 7)), x[velocity.N:]))
    p[is_vertex] = [vertex_p[(round(a, 7), round(b, 7))] for a, b in zip(X[is_vertex], Y[is_vertex])]
    np.savetxt(out_csv, np.column_stack([X, Y, u, v, p]), delimiter=",", header="x,y,u,v,p", comments="", fmt="%.17g")
print(json.dumps({"nodes": int(velocity.N) // 2, "wall": t2 - t0, "linsolve": t2 - t1}))
