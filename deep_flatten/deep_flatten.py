def deep_flatten_helper(lst):
    return_val = []
    for i in lst:
        if hasattr(i, '__iter__') and not isinstance(i, str):
            return_val += deep_flatten_helper(i)
        else:
            return_val += [i]
    return return_val


def deep_flatten(lst):
    return iter(deep_flatten_helper(lst))
