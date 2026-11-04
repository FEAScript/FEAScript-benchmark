/**
 * ════════════════════════════════════════════════════════════════
 *  FEAScript Benchmark
 *  Finite Element Simulation in JavaScript
 *  https://github.com/FEAScript/FEAScript-benchmark
 *  MIT License © 2026 FEAScript
 * ════════════════════════════════════════════════════════════════
 */

// Run one FEAScript case: node run_feascript.mjs <n> <outCsv|-> [warmRepeats]
// Lid-driven cavity, unit square, n x n quadratic (Taylor-Hood Q2-Q1) elements, viscosity 1, lid velocity 1
import { readFileSync, writeFileSync } from "node:fs";
import { resolve } from "node:path";
import { fileURLToPath, pathToFileURL } from "node:url";

// FEAScript-core checkout (FEASCRIPT_CORE, default: the sibling folder next to this repository).
// Load the built bundle, as npm and browser users do (FEASCRIPT_ENTRY=src loads the source files instead)
const core = process.env.FEASCRIPT_CORE ?? fileURLToPath(new URL("../../FEAScript-core", import.meta.url));
const entry = process.env.FEASCRIPT_ENTRY === "src" ? "src/index.js" : "dist/feascript.esm.js";
// Compatibility with older releases: before 0.3.0, FEAScript expected math.js as a global
const [major, minor] = JSON.parse(readFileSync(resolve(core, "package.json"), "utf8")).version.split(".").map(Number);
if (major === 0 && minor < 3) {
  const mathjs = process.env.FEASCRIPT_MATHJS ?? fileURLToPath(new URL("../../FEAScript-core/node_modules/mathjs/lib/esm/index.js", import.meta.url));
  globalThis.math = await import(pathToFileURL(mathjs).href);
}

const { FEAScriptModel } = await import(pathToFileURL(resolve(core, entry)).href);

const n = Number(process.argv[2]);
const outCsv = process.argv[3];
const warmRepeats = Number(process.argv[4] ?? 0);

// Silence library logging, but capture its internal console.time() splits
const timers = {};
const starts = {};
console.log = console.info = console.warn = () => {};
console.time = (label) => (starts[label] = performance.now());
console.timeEnd = (label) => (timers[label] = (performance.now() - starts[label]) / 1000);

function runOnce() {
  const model = new FEAScriptModel();
  model.setModelConfig("creepingFlowScript", { coefficientFunctions: { viscosity: 1 } });
  model.setMeshConfig({ meshDimension: "2D", elementOrder: "quadratic", numElementsX: n, numElementsY: n, maxX: 1, maxY: 1 });
  model.addBoundaryCondition("0", ["constantVelocity", 0, 0]); // Bottom
  model.addBoundaryCondition("1", ["constantVelocity", 0, 0]); // Left
  model.addBoundaryCondition("2", ["constantVelocity", 1, 0]); // Top (lid)
  model.addBoundaryCondition("3", ["constantVelocity", 0, 0]); // Right
  model.setSolverMethod("lusolve");
  const t0 = performance.now();
  const result = model.solve();
  const wall = (performance.now() - t0) / 1000;
  return { result, wall, system: timers.systemSolving ?? null };
}

const cold = runOnce();
const warm = [];
for (let i = 0; i < warmRepeats; i++) warm.push(runOnce().wall);

const { nodesCoordinates, solutionVector } = cold.result;
// Releases before 0.3.0 return no named fields: the solution vector holds u at every node, then v, then the pressure
const totalNodes = nodesCoordinates.nodesXCoordinates.length;
const fields = cold.result.fields ?? {
  u: solutionVector.slice(0, totalNodes),
  v: solutionVector.slice(totalNodes, 2 * totalNodes),
  p: new Float64Array(totalNodes).fill(NaN),
};
if (outCsv && outCsv !== "-") {
  const { nodesXCoordinates: X, nodesYCoordinates: Y } = nodesCoordinates;
  let s = "x,y,u,v,p\n";
  for (let i = 0; i < X.length; i++) s += `${X[i]},${Y[i]},${fields.u[i]},${fields.v[i]},${fields.p[i]}\n`;
  writeFileSync(outCsv, s);
}
process.stdout.write(
  JSON.stringify({ nodes: nodesCoordinates.nodesXCoordinates.length, coldWall: cold.wall, coldSystem: cold.system, warm }) + "\n",
);
