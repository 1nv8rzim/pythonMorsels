
class suppress:

    def __init__(self, *errors):
        self.errors = errors
        self.exception = None
        self.traceback = None

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, exc_traceback):
        if exc_type:
            self.exception = exc_value
            self.traceback = exc_traceback

            if exc_type in self.errors:
                return True
            else:
                for error in self.errors:
                    if issubclass(exc_type, error):
                        return True
            return False
        return True

    def __call__(self, function):
        def inside(*args, **kwargs):
            try:
                return function(*args, **kwargs)
            except self.errors:
                pass
        return inside
