// Run one FEAScript case: node run_feascript.mjs <nx> <ny> <order> <method> <outCsv|-> [warmRepeats]
import { writeFileSync } from "node:fs";
import { resolve } from "node:path";
import { fileURLToPath, pathToFileURL } from "node:url";

// FEAScript-core checkout (FEASCRIPT_CORE, default: the sibling folder next to this repository).
// Load the built bundle, as npm and browser users do (FEASCRIPT_ENTRY=src loads the source files instead)
const core = process.env.FEASCRIPT_CORE ?? fileURLToPath(new URL("../../FEAScript-core", import.meta.url));
const entry = process.env.FEASCRIPT_ENTRY === "src" ? "src/index.js" : "dist/feascript.esm.js";
const { FEAScriptModel } = await import(pathToFileURL(resolve(core, entry)).href);

const [nx, ny] = [Number(process.argv[2]), Number(process.argv[3])];
const order = process.argv[4];
const method = process.argv[5];
const outCsv = process.argv[6];
const warmRepeats = Number(process.argv[7] ?? 0);

// Silence library logging, but capture its internal console.time() splits
const timers = {};
const starts = {};
console.log = console.info = console.warn = () => {};
console.time = (label) => (starts[label] = performance.now());
console.timeEnd = (label) => (timers[label] = (performance.now() - starts[label]) / 1000);

function runOnce() {
  const model = new FEAScriptModel();
  model.setModelConfig("heatConductionScript");
  model.setMeshConfig({ meshDimension: "2D", elementOrder: order, numElementsX: nx, numElementsY: ny, maxX: 4, maxY: 2 });
  model.addBoundaryCondition("0", ["constantTemperature", 200]); // Bottom
  model.addBoundaryCondition("1", ["symmetry"]); // Left
  model.addBoundaryCondition("2", ["convection", 1, 20]); // Top
  model.addBoundaryCondition("3", ["constantTemperature", 200]); // Right
  model.setSolverMethod(method);
  const t0 = performance.now();
  const result = model.solve();
  const wall = (performance.now() - t0) / 1000;
  return { result, wall, system: timers.systemSolving ?? null, total: timers.totalSolvingTime ?? null };
}

const cold = runOnce();
const warm = [];
for (let i = 0; i < warmRepeats; i++) warm.push(runOnce().wall);

if (outCsv && outCsv !== "-") {
  const { solutionVector, nodesCoordinates } = cold.result;
  const { nodesXCoordinates: X, nodesYCoordinates: Y } = nodesCoordinates;
  let s = "x,y,T\n";
  for (let i = 0; i < solutionVector.length; i++) s += `${X[i]},${Y[i]},${solutionVector[i]}\n`;
  writeFileSync(outCsv, s);
}
process.stdout.write(
  JSON.stringify({ nodes: cold.result.solutionVector.length, coldWall: cold.wall, coldSystem: cold.system, coldTotal: cold.total, warm }) + "\n",
);
