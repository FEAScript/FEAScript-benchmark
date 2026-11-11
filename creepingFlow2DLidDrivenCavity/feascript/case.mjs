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
  // From 0.4.0 the domain is set with setGeometry and the boundaries are keyed by name; before, by numbers
  const named = typeof model.setGeometry === "function";
  if (named) {
    model.setGeometry({ rectangle: [1, 1] });
    model.setMeshConfig({ elements: "quadrilaterals", elementOrder: "quadratic", divisions: [n, n] });
  } else {
    model.setMeshConfig({ meshDimension: "2D", elementOrder: "quadratic", numElementsX: n, numElementsY: n, maxX: 1, maxY: 1 });
  }
  model.addBoundaryCondition(named ? "bottom" : "0", ["constantVelocity", 0, 0]);
  model.addBoundaryCondition(named ? "left" : "1", ["constantVelocity", 0, 0]);
  model.addBoundaryCondition(named ? "top" : "2", ["constantVelocity", 1, 0]); // The lid
  model.addBoundaryCondition(named ? "right" : "3", ["constantVelocity", 0, 0]);
  model.setSolverMethod("lusolve");
  return model;
}

export const solutionField = (result) => result.fields.u;
