from fractions import Fraction


def read_and_process():
    expr = input()
    expr = expr.replace("  ", " ")
    spaced_expr = ''
    last_digit = False

    for letter in expr:
        if letter.isdigit() or letter == '.':
            if last_digit:
                spaced_expr += letter
            else:
                if spaced_expr and spaced_expr[-1] != ' ':
                    spaced_expr += ' ' + letter
                else:
                    spaced_expr += letter
            last_digit = True
        else:
            if spaced_expr and spaced_expr[-1] != ' ' \
               and letter != ' ':
                spaced_expr += ' ' + letter
            else:
                spaced_expr += letter
            last_digit = False

    return spaced_expr


spaced_expr = read_and_process()
arr = spaced_expr.split()
nums = []
for i, item in enumerate(arr):
    if item.replace('.','').isdigit():
        nums.append(repr(Fraction(item)))
        item = '{}'
    arr[i] = item
fmt = ' '.join(arr)
print(eval(fmt.format(*nums)))
        
