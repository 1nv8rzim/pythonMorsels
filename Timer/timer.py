from time import time
from contextlib import ContextDecorator
from statistics import mean, median


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

    @property
    def median(self):
        return median(self.runs)

    @property
    def mean(self):
        return mean(self.runs)

    @property
    def min(self):
        return min(self.runs)

    @property
    def max(self):
        return max(self.runs)
