def interleave(*iterables):
    for i in zip(*iterables):
        for j in i:
            yield j
