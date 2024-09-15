def is_hidden(str1, str2):
    indices = [i for i, x in enumerate(str1) if x == str2[0]]
    if len(str2) > len(str1):
        return "NO"
    if not indices:
        return "NO"
    if len(str2) == 1:
        return "YES" if indices else "NO"
    max_step = (len(str1) - len(str2)) // (len(str2) - 1) + 1
    
    for pos in indices:
        for step in range(1, max_step + 1):
            ind = 1
            for i in range(pos + step, len(str1), step):
                if ind == len(str2):
                    return "YES"
                if str2[ind] != str1[i]:
                    break
                ind += 1
            else:
                if ind >= len(str2):
                    return "YES"
    return "NO"


str1 = [*input()]
str2 = [*input()]
print(is_hidden(str1, str2))
    
