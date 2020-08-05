from functools import wraps


class record_calls:

    def __call__(self, *args, **kwargs):
        self.call_count += 1
        return self.function(*args, **kwargs)

    def __init__(self, function):
        self.function = record_calls.test(function)
        self.call_count = 0

    @staticmethod
    def test(function):
        @wraps(function)
        def wrapper(*args, **kwargs):
            return function(*args, **kwargs)
        return wrapper
