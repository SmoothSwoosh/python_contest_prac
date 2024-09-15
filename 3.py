n = int(input())
i = n
while i < n + 3:
    j = n
    while j < n + 3:
        product = i * j
        sum = 0
        while product > 0:
            sum += product % 10
            product //= 10
        inplace = ':=)' if sum == 6 else str(i * j)
        print(i, '*', j, '=', inplace,end=' ' if j < n + 2\
                                              else '')
        j += 1
    print()
    i += 1
            
