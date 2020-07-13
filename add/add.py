def add(*args):
    shape = [len(x) for x in args[0]]
    if any([len(y) for y in x] != shape for x in args):
        raise ValueError()
    m1 = []
    for m2 in zip(*args):
        m3 = []
        for m4 in zip(*m2):
            m3.append(sum(m4))
        m1.append(m3)
    return m1
