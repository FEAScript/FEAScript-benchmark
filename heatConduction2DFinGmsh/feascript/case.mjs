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
  model.setMeshConfig({ parsedMesh: await importGmshMesh({ text: async () => content }) });
  model.addBoundaryCondition("0", ["constantTemperature", 200]); // Physical curve "bottom", tag 1
  model.addBoundaryCondition("1", ["symmetry"]); // Physical curve "left", tag 2
  model.addBoundaryCondition("2", ["convection", 1, 20]); // Physical curve "top", tag 3
  model.addBoundaryCondition("3", ["constantTemperature", 200]); // Physical curve "right", tag 4
  model.setSolverMethod(method);
  return model;
}

export const solutionField = (result) => result.solutionVector;
