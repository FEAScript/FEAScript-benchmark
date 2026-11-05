/**
 * ════════════════════════════════════════════════════════════════
 *  FEAScript Benchmark
 *  Finite Element Simulation in JavaScript
 *  https://github.com/FEAScript/FEAScript-benchmark
 *  MIT License © 2026 FEAScript
 * ════════════════════════════════════════════════════════════════
 */

// Run one FEAScript case: node run_feascript.mjs <mesh.msh> <method> <outCsv|-> [warmRepeats]
import { readFileSync, writeFileSync } from "node:fs";
import { resolve } from "node:path";
import { fileURLToPath, pathToFileURL } from "node:url";
import { makeModel } from "./case.mjs";

// FEAScript-core checkout (FEASCRIPT_CORE, default: the sibling folder next to this repository).
// Load the built bundle, as npm and browser users do (FEASCRIPT_ENTRY=src loads the source files instead)
const core = process.env.FEASCRIPT_CORE ?? fileURLToPath(new URL("../../../FEAScript-core", import.meta.url));
const entry = process.env.FEASCRIPT_ENTRY === "src" ? "src/index.js" : "dist/feascript.esm.js";
const lib = await import(pathToFileURL(resolve(core, entry)).href);

const [meshFile, method, outCsv] = process.argv.slice(2);
const warmRepeats = Number(process.argv[5] ?? 0);
const meshContent = readFileSync(meshFile, "utf8");

// Silence library logging, but capture its error messages and its internal console.time() splits
const timers = {};
const starts = {};
const errors = [];
console.log = (message) => {
  if (typeof message === "string" && message.includes("[ERROR]")) errors.push(message.replace(/^%c/, ""));
};
console.info = console.warn = () => {};
console.time = (label) => (starts[label] = performance.now());
console.timeEnd = (label) => (timers[label] = (performance.now() - starts[label]) / 1000);

async function runOnce() {
  const model = await makeModel(lib, { method }, async () => meshContent);
  const t0 = performance.now();
  const result = model.solve();
  const wall = (performance.now() - t0) / 1000;
  return { result, wall, system: timers.systemSolving ?? null };
}

const cold = await runOnce();
const warm = [];
for (let i = 0; i < warmRepeats; i++) warm.push((await runOnce()).wall);

if (outCsv && outCsv !== "-") {
  const { solutionVector, nodesCoordinates } = cold.result;
  const { nodesXCoordinates: X, nodesYCoordinates: Y } = nodesCoordinates;
  let s = "x,y,T\n";
  for (let i = 0; i < solutionVector.length; i++) s += `${X[i]},${Y[i]},${solutionVector[i]}\n`;
  writeFileSync(outCsv, s);
}
process.stdout.write(
  JSON.stringify({ nodes: cold.result.solutionVector.length, coldWall: cold.wall, coldSystem: cold.system, warm, errors }) + "\n",
);
