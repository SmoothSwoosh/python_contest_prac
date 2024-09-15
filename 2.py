sum = 0
while (num:=int(input())) > 0:
    sum += num
    if sum > 21:
        print(sum)
        break
else:
    print(num)
