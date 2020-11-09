from time import time


class Timer:
    def __init__(self):
        self.runs = []

    @property
    def elapsed(self):
        return self.runs[-1] if len(self.runs) else None

    def __enter__(self):
        self.time = time()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.runs.append(time() - self.time)
