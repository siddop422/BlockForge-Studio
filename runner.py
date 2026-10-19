#!/usr/bin/env python3
"""Optional localhost runner for BlockForge Studio (Python standard library only).

WARNING: generated programs execute with the current user's operating-system
permissions. This runner adds request limits, a temporary working directory,
and a timeout, but it is NOT a security sandbox. Run only code you trust.
"""
from __future__ import annotations

import json
import os
import subprocess
import sys
import tempfile
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parent
HTML_FILE = ROOT / "blockforge_studio.html"
HOST = "127.0.0.1"
PORT = 8765
MAX_REQUEST_BYTES = 100_000
MAX_SOURCE_CHARS = 80_000
MAX_OUTPUT_CHARS = 64_000
TIMEOUT_SECONDS = 5


def _limited(text: str, limit: int = MAX_OUTPUT_CHARS) -> tuple[str, bool]:
    if len(text) <= limit:
        return text, False
    return text[:limit], True


def execute_python(source: str, timeout: float = TIMEOUT_SECONDS) -> dict[str, Any]:
    """Execute user-provided Python with bounded time/output and a temporary cwd.

    This is resource limiting, not a security boundary: Python code still runs
    with the current user's permissions and may access the network/filesystem.
    """
    if not isinstance(source, str):
        raise ValueError("The code field must be a string.")
    if not source.strip():
        raise ValueError("There is no Python code to run.")
    if len(source) > MAX_SOURCE_CHARS:
        raise ValueError(f"Python source exceeds the {MAX_SOURCE_CHARS:,}-character limit.")

    env = {"PYTHONIOENCODING": "utf-8"}
    for key in ("PATH", "SYSTEMROOT", "WINDIR", "TEMP", "TMP", "HOME"):
        if os.environ.get(key):
            env[key] = os.environ[key]

    with tempfile.TemporaryDirectory(prefix="blockforge-run-") as workdir:
        try:
            result = subprocess.run(
                [sys.executable, "-I", "-u", "-c", source],
                cwd=workdir,
                env=env,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True,
                encoding="utf-8",
                errors="replace",
                timeout=timeout,
                check=False,
            )
            stdout, cut_out = _limited(result.stdout)
            stderr, cut_err = _limited(result.stderr)
            return {
                "stdout": stdout,
                "stderr": stderr,
                "returncode": result.returncode,
                "timed_out": False,
                "truncated": cut_out or cut_err,
            }
        except subprocess.TimeoutExpired as exc:
            stdout = exc.stdout or ""
            stderr = exc.stderr or ""
            if isinstance(stdout, bytes):
                stdout = stdout.decode("utf-8", errors="replace")
            if isinstance(stderr, bytes):
                stderr = stderr.decode("utf-8", errors="replace")
            stdout, cut_out = _limited(stdout)
            stderr, cut_err = _limited(stderr)
            return {
                "stdout": stdout,
                "stderr": stderr,
                "returncode": None,
                "timed_out": True,
                "truncated": cut_out or cut_err,
            }


class Handler(BaseHTTPRequestHandler):
    server_version = "BlockForgeLocalRunner/1.0"

    def _send_json(self, status: int, payload: dict[str, Any]) -> None:
        body = json.dumps(payload, ensure_ascii=False).encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.send_header("Cache-Control", "no-store")
        self.send_header("X-Content-Type-Options", "nosniff")
        self.end_headers()
        self.wfile.write(body)

    def _origin_allowed(self) -> bool:
        origin = self.headers.get("Origin")
        return origin is None or origin in {
            f"http://127.0.0.1:{PORT}",
            f"http://localhost:{PORT}",
        }

    def do_GET(self) -> None:  # noqa: N802
        if self.path == "/api/health":
            self._send_json(200, {"ok": True, "python": sys.version.split()[0]})
            return
        if self.path in ("/", "/blockforge_studio.html"):
            try:
                body = HTML_FILE.read_bytes()
            except OSError:
                self._send_json(500, {"error": "Could not read blockforge_studio.html beside runner.py."})
                return
            self.send_response(200)
            self.send_header("Content-Type", "text/html; charset=utf-8")
            self.send_header("Content-Length", str(len(body)))
            self.send_header("Cache-Control", "no-store")
            self.send_header("X-Content-Type-Options", "nosniff")
            self.end_headers()
            self.wfile.write(body)
            return
        self._send_json(404, {"error": "Not found."})

    def do_POST(self) -> None:  # noqa: N802
        if self.path != "/api/run":
            self._send_json(404, {"error": "Not found."})
            return
        if not self._origin_allowed():
            self._send_json(403, {"error": "Cross-origin requests are not allowed."})
            return
        content_type = self.headers.get("Content-Type", "").split(";", 1)[0].strip().lower()
        if content_type != "application/json":
            self._send_json(415, {"error": "Send application/json."})
            return
        try:
            length = int(self.headers.get("Content-Length", "0"))
        except ValueError:
            self._send_json(400, {"error": "Invalid Content-Length."})
            return
        if length <= 0 or length > MAX_REQUEST_BYTES:
            self._send_json(413, {"error": f"Request must be between 1 and {MAX_REQUEST_BYTES:,} bytes."})
            return
        try:
            payload = json.loads(self.rfile.read(length).decode("utf-8"))
            if not isinstance(payload, dict):
                raise ValueError("Request body must be a JSON object.")
            result = execute_python(payload.get("code"))
        except (UnicodeDecodeError, json.JSONDecodeError, ValueError) as exc:
            self._send_json(400, {"error": str(exc)})
            return
        self._send_json(200, result)

    def log_message(self, fmt: str, *args: Any) -> None:
        # Do not print program source or output into the terminal log.
        super().log_message(fmt, *args)


def main() -> None:
    if not HTML_FILE.is_file():
        raise SystemExit(f"Missing {HTML_FILE.name}. Keep runner.py beside the HTML editor.")
    server = ThreadingHTTPServer((HOST, PORT), Handler)
    print("BlockForge local runner")
    print(f"Open http://{HOST}:{PORT}/ in your browser.")
    print("Press Ctrl+C to stop. Run only Python code you trust.")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nStopping BlockForge runner…")
    finally:
        server.server_close()


if __name__ == "__main__":
    main()
