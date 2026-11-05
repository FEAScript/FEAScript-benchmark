#!/usr/bin/env python3
# ════════════════════════════════════════════════════════════════
#  FEAScript Benchmark
#  Finite Element Simulation in JavaScript
#  https://github.com/FEAScript/FEAScript-benchmark
#  MIT License © 2026 FEAScript
# ════════════════════════════════════════════════════════════════

"""Run every benchmark for a FEAScript version: benchmarks, reports and the speed-up plots by version.

Build FEAScript-core first (npm run build), then run this with the Python that has the benchmark packages:

    FEASCRIPT_VERSION=0.4.0 ~/.venvs/feascript-benchmark/bin/python run_all.py

Without FEASCRIPT_VERSION, the version comes from FEAScript-core/package.json. Add benchmark names to run only those.
"""
import json, os, re, subprocess, sys

HERE = os.path.dirname(os.path.abspath(__file__))
BENCHMARKS = ["heatConduction2DFin", "heatConduction2DFinGmsh", "creepingFlow2DLidDrivenCavity"]
HISTORY = ["heatConduction2DFin", "creepingFlow2DLidDrivenCavity"]  # Benchmarks with results from several versions

core = os.path.abspath(os.environ.get("FEASCRIPT_CORE") or os.path.join(HERE, "..", "FEAScript-core"))
version = os.environ.get("FEASCRIPT_VERSION") or json.load(open(os.path.join(core, "package.json")))["version"]
cpu = subprocess.run("lscpu | sed -n 's/^Model name: *//p'", shell=True, capture_output=True, text=True).stdout.strip()
machine = os.environ.get("FEASCRIPT_MACHINE") or re.sub(r"[^a-z0-9]+", "-", re.sub(r"\((r|tm)\)|\d+-core processor", "", cpu.lower())).strip("-")
env = {**os.environ, "FEASCRIPT_VERSION": version, "FEASCRIPT_MACHINE": machine}

for bench in sys.argv[1:] or BENCHMARKS:
    folder = os.path.join(HERE, bench)
    run = os.path.join(folder, "reports", machine, version)
    os.makedirs(run, exist_ok=True)
    print(f"=== {bench}: FEAScript {version} on {machine}", flush=True)
    with open(os.path.join(run, "run.log"), "w") as log:
        subprocess.run([sys.executable, "benchmark.py"], cwd=folder, env=env, stdout=log, stderr=subprocess.STDOUT, check=True)
    subprocess.run([sys.executable, "make_report.py", machine, version], cwd=folder, env=env, stdout=subprocess.DEVNULL, check=True)
    if bench in HISTORY:
        subprocess.run([sys.executable, os.path.join(HERE, "make_history.py"), bench], stdout=subprocess.DEVNULL, check=True)
