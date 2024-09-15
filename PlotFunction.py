from math import *

w, h, a, b, func = input().split()


def f(x):
    return eval(func)


w, h, a, b = map(int, [w, h, a, b])
canvas = [[' '] * (w + 1) for i in range(h + 1)]

xs = [i * (b - a) / w + a for i in range(w + 1)]
ys = [f(x) for x in xs]

xs = [x - a for x in xs]
ys = [y - min(ys) for y in ys]

ys = [round(y * h / max(ys)) for y in ys]

for i in range(1, w + 1):
    canvas[h - ys[i]][i]= '*'
    step = 1 if ys[i - 1] <= ys[i] else -1
    for j in range(ys[i - 1], ys[i], step):
        canvas[h - j][i - 1] = '*'

for line in canvas:
    print(*line,sep='')
