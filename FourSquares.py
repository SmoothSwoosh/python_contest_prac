from math import isqrt

n = int(input())
x_bound = isqrt(n) + 1
for x in range(0, x_bound):
    y_bound = min(x, isqrt(n - x * x)) + 1
    for y in range(0, y_bound):
        z_bound = min(y, isqrt(n - x * x - y * y)) + 1
        for z in range(0, z_bound):
            t = isqrt(n - x * x - y * y - z * z)
            if t * t == n - x * x - y * y - z * z\
               and x >= y >= z >= t:
                print(*sorted([x, y, z, t], reverse=True))
