def tail(sequence, elements):
    if elements < 1:
        return []
    try:
        return list(sequence[-elements:])
    except:
        return tail([x for x in sequence], elements)
