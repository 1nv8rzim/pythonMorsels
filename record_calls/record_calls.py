from functools import wraps

NO_RETURN = object()


class Call:
    def __init__(self, args, kwargs, return_value, exception):
        self.args = args
        self.kwargs = kwargs
        self.return_value = return_value
        self.exception = exception


def record_calls(function):
    @wraps(function)
    def wrapper(*args, **kwargs):
        wrapper.call_count += 1
        try:
            return_value = function(*args, **kwargs)
        except Exception as e:
            wrapper.calls.append(Call(args, kwargs, NO_RETURN, e))
            raise(e)
        wrapper.calls.append(Call(args, kwargs, return_value, None))
        return return_value

    wrapper.call_count = 0
    wrapper.calls = []

    return wrapper
