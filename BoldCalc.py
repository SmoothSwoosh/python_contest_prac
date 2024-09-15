import re

values = {}
eq = ''
def calculate():
    if re.search(r'\w\(', eq) or '**' in eq or '//' in eq:
        print('Syntax error')
        return

    operations = '+-*/%()'
    notation = ''
    for char in eq:
        if char in operations:
            notation = notation + ' ' + char + ' '
        else:
            notation += char
            
    notation = notation.split()
    for i, operand in enumerate(notation):
        if operand in operations:
            notation[i] = '//' if operand == '/' else notation[i]
        elif operand.isidentifier():
            if not '_' + operand in values.keys():
                print('Name error')
                return
            else:
                notation[i] = '_' + notation[i]
        else:
            if not operand.isdigit():
                print('Syntax error')
                return

    try:
        return eval(''.join(notation), values)
    except:
        print('Runtime error')
        return


while s := input():
    if s[0] == '#':
        continue
    s = s.replace(' ', '')
    if s.count('=') > 1:
        print('Syntax error')
    elif s.count('=') == 1:
        var, eq = s.split('=')
        if not var.isidentifier():
            print('Assignment error')
        else:
            val = calculate()
            if val != None:
                values['_' + var] = val
    else:
        eq = s
        val = calculate()
        if val != None:
            print(val)
