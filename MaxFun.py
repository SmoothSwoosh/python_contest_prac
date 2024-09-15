def maxfun(s, f1, *functions):
    return max(reversed((f1,) + functions), key=lambda f: sum(map(f, s)))
