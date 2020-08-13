def deep_flatten(lst):
    return_val = []
    for i in lst:
        if hasattr(i, '__iter__') and not isinstance(i, str):
            for i in deep_flatten(i):
                yield i
        else:
            yield i
