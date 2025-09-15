import subprocess
import threading
from unittest import result

class GforthProcess:
    def __init__(self, gforth_path="gforth"):
        self.process = subprocess.Popen(
            [gforth_path],
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            bufsize=1
        )

        self.output = ""
        self.lock = threading.Lock()
        self.reader_thread = threading.Thread(target=self._read_output, daemon=True)
        self.reader_thread.start()

        self.error_thread = threading.Thread(target=self._read_error, daemon=True)
        self.error_thread.start()

    def _read_output(self):
        for line in self.process.stdout:
            with self.lock:
                self.output += line

    def _read_error(self):
        for line in self.process.stderr:
            with self.lock:
                self.output += line

    def send_code(self, code: str) -> str:
        with self.lock:
            self.output = ""
        self.process.stdin.write(code + "\n")
        self.process.stdin.flush()
        # Wait briefly for output (can be improved)
        threading.Event().wait(0.1)
        with self.lock:
            return self.output.strip()

    def close(self):
        self.process.terminate()


if __name__ == "__main__":
    import time

    gforth = GforthProcess()
    time.sleep(1.0)
    print(gforth.output)
    try:
        for i in range(10):
            forth_code = input(">")
            if forth_code.lower() in ("exit", "quit"): break
            result = gforth.send_code(forth_code)
            print("Output:", result)
    finally:
        gforth.close()