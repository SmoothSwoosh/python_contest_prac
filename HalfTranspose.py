a = []
tmp = input()
if tmp:
    tmp = list(eval(tmp))
    a.append(tmp)
    l = len(tmp)
    for i in range(l - 1):
        tmp = list(eval(input()))
        a.append(tmp)

    for i in range(l):
        line = []
        for j in range(i + 1):
            line.append(a[i][j])
        for j in range(i - 1, -1, -1):
            line.append(a[j][i])
        print(*line, sep=',')

