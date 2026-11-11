/**
 * ════════════════════════════════════════════════════════════════
 *  FEAScript Benchmark
 *  Finite Element Simulation in JavaScript
 *  https://github.com/FEAScript/FEAScript-benchmark
 *  MIT License © 2026 FEAScript
 * ════════════════════════════════════════════════════════════════
 */

// The fin on a Gmsh mesh, built the same way in Node.js and in a browser. readMesh returns the text of a mesh file
export async function makeModel({ FEAScriptModel, importGmshMesh }, { mesh, method }, readMesh) {
  const content = await readMesh(mesh);
  const model = new FEAScriptModel();
  model.setModelConfig("heatConductionScript");
  const parsedMesh = await importGmshMesh({ text: async () => content });
  // From 0.4.0 a mesh is set with setMesh and its boundaries are keyed by the names of the physical curves;
  // before, by their tag minus one (bottom 1, left 2, top 3, right 4)
  const named = typeof model.setMesh === "function";
  if (named) model.setMesh(parsedMesh);
  else model.setMeshConfig({ parsedMesh });
  model.addBoundaryCondition(named ? "bottom" : "0", ["constantTemperature", 200]);
  model.addBoundaryCondition(named ? "left" : "1", ["symmetry"]);
  model.addBoundaryCondition(named ? "top" : "2", ["convection", 1, 20]);
  model.addBoundaryCondition(named ? "right" : "3", ["constantTemperature", 200]);
  model.setSolverMethod(method);
  return model;
}

export const solutionField = (result) => result.solutionVector;
