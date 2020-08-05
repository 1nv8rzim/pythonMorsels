class record_calls:
    def __call__(self, *args, **kwargs):
        self.call_count += 1
        return self.function(*args, *kwargs)

    def __init__(self, function):
        self.function = function
        self.call_count = 0
