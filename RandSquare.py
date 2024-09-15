from random import *
from math import *


def randsquare(A, B):
    (x0, y0), (x1, y1), k = A, B, random()
    d_point = (x0 + (x1 - x0) * k, y0 + (y1 - y0) * k)
    d_len = sqrt((x1 - x0) ** 2 + (y1 - y0) ** 2)
    normal = (y0 - y1, x1 - x0)
    nearest = (x0, y0) if ((x0 - d_point[0]) ** 2 + (y0 - d_point[1]) ** 2) \
                      < ((x1 - d_point[0]) ** 2 + (y1 - d_point[1]) ** 2) else (x1, y1)
    normal_height = uniform(0, sqrt((nearest[0] - d_point[0]) ** 2 + (nearest[1] - d_point[1]) ** 2))
    t = choice([-1, 1]) / d_len
    return (d_point[0] + t * normal_height * normal[0], d_point[1] + t * normal_height * normal[1])
