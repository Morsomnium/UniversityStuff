import math


def fun_z(x, y):
    z = ((5 / x) * (((x ** 2) + (y ** 2)) ** (1. / 3.))) / (7 * (math.cos((math.pi * x)) ** 2))
    return z
