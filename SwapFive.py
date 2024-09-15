def swap_five(k, prev, add = 0):
    div, mod = divmod(prev * k + add, 10)
    if mod == k and div == 0:
        return
    swap_five(k, mod, div)
    print(mod,end='')

k = int(input())
swap_five(k, k)
print(k)
