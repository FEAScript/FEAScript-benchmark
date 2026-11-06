# ════════════════════════════════════════════════════════════════
#  FEAScript Benchmark
#  Finite Element Simulation in JavaScript
#  https://github.com/FEAScript/FEAScript-benchmark
#  MIT License © 2026 FEAScript
# ════════════════════════════════════════════════════════════════

"""Run the cases of a benchmark in fresh headless browsers.

A local server gives the browser the page, FEAScript's built bundle and the case of the benchmark, and takes the
times and the solution that the page posts back. No JavaScript packages are needed.
"""
import json, os, re, shutil, signal, statistics, subprocess, tempfile, threading, time
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from urllib.parse import quote
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
CHROMIUM = os.environ.get("CHROMIUM_PATH", "chromium")
FIREFOX = os.environ.get("FIREFOX_PATH", "firefox")
TIMEOUT = int(os.environ.get("BROWSER_TIMEOUT", 1800))  # seconds per browser run


def sh(*cmd):
    return subprocess.run(cmd, capture_output=True, text=True).stdout.strip()


def versions():
    return {"chromium": re.search(r"[\d.]+", sh(CHROMIUM, "--version")).group(0), "firefox": re.search(r"[\d.]+", sh(FIREFOX, "--version")).group(0)}


class Server(BaseHTTPRequestHandler):
    """Serves the page, FEAScript's bundle, the case and its meshes, and takes the result of a run."""
    core = case_file = mesh_dir = result = None
    done = threading.Event()

    def do_GET(self):
        path = self.path.split("?")[0]
        file = (os.path.join(HERE, "page.html") if path == "/" else
                Server.case_file if path == "/case.mjs" else
                os.path.join(Server.core, "dist", path[len("/core/"):]) if path.startswith("/core/") else
                os.path.join(Server.mesh_dir or "", path[len("/mesh/"):]) if path.startswith("/mesh/") else None)
        if not file or not os.path.isfile(file):
            self.send_error(404)
            return
        self.send_response(200)
        self.send_header("Content-Type", "text/html" if file.endswith(".html") else "text/plain" if file.endswith(".msh") else "text/javascript")
        # Cross-origin isolation gives the page the finest timers
        self.send_header("Cross-Origin-Opener-Policy", "same-origin")
        self.send_header("Cross-Origin-Embedder-Policy", "require-corp")
        self.send_header("Cache-Control", "no-store")
        self.end_headers()
        with open(file, "rb") as f:
            shutil.copyfileobj(f, self.wfile)

    def do_POST(self):
        Server.result = json.loads(self.rfile.read(int(self.headers["Content-Length"])))
        self.send_response(204)
        self.end_headers()
        Server.done.set()

    def log_message(self, *args):
        pass


def command(browser, profile, url):
    if browser == "chromium":
        return [CHROMIUM, "--headless=new", f"--user-data-dir={profile}", "--no-first-run", "--no-default-browser-check", "--disable-gpu",
                "--disable-extensions", "--disable-background-networking", "--disable-component-update", "--disable-sync", url]
    prefs = {"app.update.enabled": False, "browser.shell.checkDefaultBrowser": False, "datareporting.policy.dataSubmissionEnabled": False,
             "toolkit.telemetry.enabled": False, "browser.aboutwelcome.enabled": False, "browser.startup.homepage_override.mstone": "ignore"}
    with open(os.path.join(profile, "user.js"), "w") as f:
        f.writelines(f"user_pref({json.dumps(k)}, {json.dumps(v)});\n" for k, v in prefs.items())
    return [FIREFOX, "--headless", "--no-remote", "--new-instance", "--profile", profile, url]


def run_once(browser, port, params, warm, pin):
    """One run in a fresh browser with an empty profile."""
    profile = tempfile.mkdtemp(prefix="feascript-browser-")
    url = f"http://127.0.0.1:{port}/?params={quote(json.dumps(params))}&warm={warm}"
    Server.done.clear()
    t0 = time.perf_counter()
    p = subprocess.Popen(pin + command(browser, profile, url), stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, start_new_session=True)
    try:
        if not Server.done.wait(TIMEOUT):
            raise RuntimeError(f"timeout after {TIMEOUT} s")
        process = time.perf_counter() - t0
    finally:
        os.killpg(p.pid, signal.SIGKILL)
        p.wait()
        shutil.rmtree(profile, ignore_errors=True)
    r = Server.result
    if "error" in r:
        raise RuntimeError(r["error"])
    r["process"] = process
    return r


def run_cases(cases, case_file, core, run_dir, feascript_results, pin, reps, warm, mesh_dir=None):
    """Run the cases in each browser. Each case is a dict with name, code, group, params and reference (the Node.js solution).

    Writes <run_dir>/browsers.json and <feascript_results>/<browser>/<version>/results.json.
    """
    Server.core, Server.case_file, Server.mesh_dir = core, case_file, mesh_dir
    server = ThreadingHTTPServer(("127.0.0.1", 0), Server)
    threading.Thread(target=server.serve_forever, daemon=True).start()
    port = server.server_address[1]
    found = versions()
    rows, agents, isolated = [], {}, {}
    for case in cases:
        for browser, version in found.items():
            base = {"case": case["name"], "code": case["code"], "group": case["group"], "runtime": browser, "runtimeVersion": version}
            try:
                # Slow cases (over 20 s) are timed once, with a single repeated solve. It is in a run of its own, so as not to count against the time limit
                first = run_once(browser, port, case["params"], 0, pin)
                runs = [first]
                if first["coldWall"] <= 20:
                    first["warm"] = (repeated := run_once(browser, port, case["params"], warm, pin))["warm"]
                    runs += [repeated] + [run_once(browser, port, case["params"], 0, pin) for _ in range(reps - 2)]
                else:
                    try:
                        first["warm"] = run_once(browser, port, case["params"], 1, pin)["warm"]
                    except RuntimeError as e:  # The first solve is still a valid measurement
                        base["noRepeat"] = str(e)[:200]
                        print(f"{browser} {case['name']} {case['code']} no repeated solve: {str(e)[:300]}", flush=True)
            except RuntimeError as e:
                rows.append({**base, "failed": str(e)[:200]})
                print(f"{browser} {case['name']} {case['code']} failed: {str(e)[:300]}", flush=True)
                continue
            agents[browser], isolated[browser] = first["userAgent"], first["crossOriginIsolated"]
            solution = np.array(first["solution"])
            row = {**base, "nodes": case["nodes"], "solve": statistics.median(r["coldWall"] for r in runs), "process": statistics.median(r["process"] for r in runs),
                   "warmWall": statistics.median(first["warm"]) if first["warm"] else None, "nruns": len(runs),
                   "maxDiffVsNode": float(np.max(np.abs(solution - case["reference"])))}
            rows.append(row)
            print(json.dumps(row), flush=True)
    server.shutdown()
    # Keep the cases that this run did not repeat
    path = os.path.join(run_dir, "browsers.json")
    old = json.load(open(path)) if os.path.exists(path) else {"rows": [], "userAgents": {}, "crossOriginIsolated": {}}
    rows = list({(r["case"], r["code"], r["runtime"]): r for r in old["rows"] + rows}.values())
    with open(path, "w") as f:
        json.dump({"versions": found, "userAgents": {**old["userAgents"], **agents}, "crossOriginIsolated": {**old["crossOriginIsolated"], **isolated}, "rows": rows}, f, indent=1)
    for browser, version in found.items():
        out = os.path.join(feascript_results, browser, version)
        os.makedirs(out, exist_ok=True)
        with open(os.path.join(out, "results.json"), "w") as f:
            json.dump([r for r in rows if r["runtime"] == browser], f, indent=1)
