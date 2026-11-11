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
  // From 0.4.0 the domain is set with setGeometry and the boundaries are keyed by name; before, by numbers
  const named = typeof model.setGeometry === "function";
  if (named) {
    model.setGeometry({ rectangle: [4, 2] });
    model.setMeshConfig({ elements: "quadrilaterals", elementOrder: order, divisions: [nx, ny] });
  } else {
    model.setMeshConfig({ meshDimension: "2D", elementOrder: order, numElementsX: nx, numElementsY: ny, maxX: 4, maxY: 2 });
  }
  model.addBoundaryCondition(named ? "bottom" : "0", [constantTemperature, 200]);
  model.addBoundaryCondition(named ? "left" : "1", ["symmetry"]);
  model.addBoundaryCondition(named ? "top" : "2", ["convection", 1, 20]);
  model.addBoundaryCondition(named ? "right" : "3", [constantTemperature, 200]);
  model.setSolverMethod(method);
  return model;
}

export const solutionField = (result) => result.solutionVector;
