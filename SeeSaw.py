def seesaw(sequence):
    odds, evens = [], []
    for num in sequence:
        if num % 2:
            odds.append(num)
        else:
            evens.append(num)

    yield_even = True
    k_even, k_odd = 0, 0
    while k_even < len(evens) and k_odd < len(odds):
        if yield_even:
            yield evens[k_even]
            k_even += 1
        else:
            yield odds[k_odd]
            k_odd += 1
        yield_even = not yield_even

    lst = odds if k_odd < len(odds) else evens
    ind = k_even if k_even < len(evens) else k_odd
    for i in range(ind, len(lst)):
        yield lst[i]


