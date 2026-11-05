/**
 * ════════════════════════════════════════════════════════════════
 *  FEAScript Benchmark
 *  Finite Element Simulation in JavaScript
 *  https://github.com/FEAScript/FEAScript-benchmark
 *  MIT License © 2026 FEAScript
 * ════════════════════════════════════════════════════════════════
 */

// The fin, built the same way in Node.js and in a browser. constantTemperature is the name of that condition in the
// release: "constantTemp" before 0.3.0
export function makeModel({ FEAScriptModel }, { nx, ny, order, method, constantTemperature = "constantTemperature" }) {
  const model = new FEAScriptModel();
  model.setModelConfig("heatConductionScript");
  model.setMeshConfig({ meshDimension: "2D", elementOrder: order, numElementsX: nx, numElementsY: ny, maxX: 4, maxY: 2 });
  model.addBoundaryCondition("0", [constantTemperature, 200]); // Bottom
  model.addBoundaryCondition("1", ["symmetry"]); // Left
  model.addBoundaryCondition("2", ["convection", 1, 20]); // Top
  model.addBoundaryCondition("3", [constantTemperature, 200]); // Right
  model.setSolverMethod(method);
  return model;
}

export const solutionField = (result) => result.solutionVector;
