def interleave(a, b):
    return_val = []
    for i, j in zip(a, b):
        return_val.append(i)
        return_val.append(j)
    return return_val
