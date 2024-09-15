p, b, g, e = input()

first, second = {}, {}
last_is_p = False
while s := input():
    line = s.split()
    for word in line:
        if word[0] == g and word[-1] == e:
            second[word] = second.get(word, 0) + 1
        if word[0] == b and last_is_p:
            first[word] = first.get(word, 0) + 1
        last_is_p = word[-1] == p

p_ans = max(first.items(), key=lambda x: x[1]) if first \
                                                else ('...', 0)
e_ans = max(second.items(), key=lambda x: x[1]) if second \
                                                else ('...', 0)

print(*p_ans, '-', *e_ans)


            


