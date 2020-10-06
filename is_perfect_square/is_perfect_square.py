from math import sqrt


def is_perfect_square(num):
    if num < 0:
        return False
    return sqrt(num).is_integer()
