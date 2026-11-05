/**
 * ════════════════════════════════════════════════════════════════
 *  FEAScript Benchmark
 *  Finite Element Simulation in JavaScript
 *  https://github.com/FEAScript/FEAScript-benchmark
 *  MIT License © 2026 FEAScript
 * ════════════════════════════════════════════════════════════════
 */

// The lid-driven cavity, built the same way in Node.js and in a browser
export function makeModel({ FEAScriptModel }, { n }) {
  const model = new FEAScriptModel();
  model.setModelConfig("creepingFlowScript", { coefficientFunctions: { viscosity: 1 } });
  model.setMeshConfig({ meshDimension: "2D", elementOrder: "quadratic", numElementsX: n, numElementsY: n, maxX: 1, maxY: 1 });
  model.addBoundaryCondition("0", ["constantVelocity", 0, 0]); // Bottom
  model.addBoundaryCondition("1", ["constantVelocity", 0, 0]); // Left
  model.addBoundaryCondition("2", ["constantVelocity", 1, 0]); // Top (lid)
  model.addBoundaryCondition("3", ["constantVelocity", 0, 0]); // Right
  model.setSolverMethod("lusolve");
  return model;
}

export const solutionField = (result) => result.fields.u;
