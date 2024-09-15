def nomore(sequence):
    for num in sequence:
        for candidate in sequence:
            if num >= candidate:
                yield candidate
