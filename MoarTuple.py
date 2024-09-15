def moar(a, b, n):
    divs_a, divs_b = 0, 0
    for num in a:
        divs_a += num % n == 0
    for num in b:
        divs_b += num % n == 0
    return divs_a > divs_b
