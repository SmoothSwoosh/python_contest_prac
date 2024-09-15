from decimal import *


getcontext().prec = 10000


def factorial(k):
    if k == 0:
        return 1
    n = 1
    fact = 1
    for i in range(k):
        fact *= n
        n += 1
    return fact


def PiGen():
    numerator = Decimal(10005).sqrt() * 426880
    amount = 0
    k = 0
    
    while True:
        amount += Decimal(factorial(6*k) * (545140134 * k + 13591409)) \
                  / Decimal(factorial(3*k) * (factorial(k)**3) * ((-262537412640768000)**k))
        k += 1
        yield numerator / amount
