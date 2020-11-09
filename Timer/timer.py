from time import time
from contextlib import ContextDecorator


class Timer(ContextDecorator):
    def __init__(self, function=None):
        self.runs = []
        self.function = function

    @property
    def elapsed(self):
        return self.runs[-1] if len(self.runs) else None

    def __enter__(self):
        self.time = time()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.runs.append(time() - self.time)

    def __call__(self, *args, **kwargs):
        self.time = time()
        return_value = self.function(*args, **kwargs)
        self.runs.append(time() - self.time)
        return return_value
