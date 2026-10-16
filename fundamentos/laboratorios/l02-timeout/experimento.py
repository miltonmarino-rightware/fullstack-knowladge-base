"""Laboratório local L02. Apenas biblioteca padrão; não é servidor de produção."""
import hashlib
import http.client
import json
import platform
import sqlite3
import tempfile
import threading
import time
from datetime import datetime, timezone
from http.server import BaseHTTPRequestHandler, HTTPServer
from pathlib import Path


def execute_case(db_path, operation_id, delay, timeout):
    events = []
    lock = threading.Lock()
    started = time.monotonic()
    finished = threading.Event()

    def record(name, **data):
        with lock:
            events.append({"event": name,
                           "elapsed_ms": round((time.monotonic() - started) * 1000, 3),
                           **data})

    class Handler(BaseHTTPRequestHandler):
        protocol_version = "HTTP/1.1"

        def log_message(self, *args):
            pass

        def do_POST(self):
            try:
                self.rfile.read(int(self.headers.get("Content-Length", "0")))
                record("server_received", operation_id=operation_id)
                with sqlite3.connect(db_path) as db:
                    db.execute("INSERT INTO operations VALUES (?)", (operation_id,))
                record("database_commit_returned")
                time.sleep(delay)  # Falha temporal deliberada, depois do commit.
                payload = json.dumps({"operation_id": operation_id}).encode()
                record("server_response_attempt")
                try:
                    self.send_response(201)
                    self.send_header("Content-Type", "application/json")
                    self.send_header("Content-Length", str(len(payload)))
                    self.send_header("Connection", "close")
                    self.end_headers()
                    self.wfile.write(payload)
                    self.wfile.flush()
                    record("server_write_returned")
                except OSError as error:
                    record("server_write_error", error_type=type(error).__name__)
                self.close_connection = True
            except Exception as error:
                record("server_error", error_type=type(error).__name__)
            finally:
                finished.set()

    server = HTTPServer(("127.0.0.1", 0), Handler)
    worker = threading.Thread(target=server.serve_forever, daemon=True)
    worker.start()
    connection = http.client.HTTPConnection("127.0.0.1", server.server_port,
                                            timeout=timeout)
    outcome, status, body = None, None, None
    try:
        record("client_send")
        connection.request("POST", "/operations", body=b"{}",
                           headers={"Content-Type": "application/json"})
        try:
            response = connection.getresponse()
            status = response.status
            body = json.loads(response.read())
            outcome = "response_received"
            record("client_response_received", status=status)
        except TimeoutError:
            outcome = "timeout"
            record("client_timeout")
        finally:
            connection.close()

        # Nova conexão SQLite: consulta independente do caminho HTTP.
        with sqlite3.connect(db_path) as db:
            count = db.execute("SELECT COUNT(*) FROM operations WHERE id = ?",
                               (operation_id,)).fetchone()[0]
        record("independent_database_read", matching_rows=count)
        if not finished.wait(delay + timeout + 3):
            raise RuntimeError("O servidor não terminou dentro do limite do laboratório")
    finally:
        connection.close()
        server.shutdown()
        server.server_close()
        worker.join(timeout=3)

    names = [event["event"] for event in events]
    expected_outcome = "timeout" if delay > timeout else "response_received"
    passed = count == 1 and outcome == expected_outcome and "server_error" not in names
    if expected_outcome == "timeout":
        passed = passed and names.index("database_commit_returned") < names.index("client_timeout")
        passed = passed and names.index("client_timeout") < names.index("server_response_attempt")
    else:
        passed = passed and status == 201 and body == {"operation_id": operation_id}
    return {"operation_id": operation_id, "response_delay_seconds": delay,
            "client_timeout_seconds": timeout, "client_outcome": outcome,
            "matching_rows": count, "passed": passed, "events": events}


def main():
    with tempfile.TemporaryDirectory(prefix="rightware-l02-") as directory:
        db_path = str(Path(directory) / "operations.sqlite3")
        with sqlite3.connect(db_path) as db:
            db.execute("CREATE TABLE operations (id TEXT PRIMARY KEY)")
        cases = [execute_case(db_path, "control-fast", 0, 2),
                 execute_case(db_path, "delayed-response", 1, 0.2)]
    report = {"lab": "FND-001-L02", "executed_at_utc": datetime.now(timezone.utc).isoformat(),
              "environment": {"python": platform.python_version(),
                              "system": platform.system(), "release": platform.release(),
                              "sqlite": sqlite3.sqlite_version},
              "script_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
              "scope": "loopback HTTP/1.1 + SQLite; no crash, proxy, TLS or retry",
              "cases": cases, "passed": all(case["passed"] for case in cases)}
    print(json.dumps(report, ensure_ascii=False, indent=2))
    raise SystemExit(0 if report["passed"] else 1)


if __name__ == "__main__":
    main()
