from itertools import zip_longest


def interleave(*iterables):
    temp = object()
    for i in zip_longest(*iterables, fillvalue=temp):
        for j in i:
            if j is not temp:
                yield j
