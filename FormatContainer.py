container = []
water, gas = 0, 0
diagram_width = 20

#read and calculate count of liquid and gas
while line := input():
    container.append([*line])
    water += container[-1].count('~')
    gas += container[-1].count('.')

#transpose container and calculate its volume
w, h = len(container), len(container[0])
volume = (w - 2) * (h - 2)
t_container = [['#'] * w for i in range(h)]

#add liquid if a top layer isn't filled
gas -= gas % (w - 2)
water = volume - gas

#fill transposed container
filled_gas = 0
for i in range(1, h - 1):
    for j in range(1, w - 1):
        if gas > filled_gas:
            t_container[i][j] = '.'
            filled_gas += 1
        else:
            t_container[i][j] = '~'

#print transposed container
for i in range(h):
    print(''.join(t_container[i]))

#calculate proportion between liquid and gas
align = len(str(water)) if water > gas else len(str(gas))

#print diagram
if water > gas:
    water_part = diagram_width
    gas_part = round(diagram_width * gas / water)
else:
    water_part = round(diagram_width * water / gas)
    gas_part = diagram_width

print(f'{"." * gas_part:20}', f'{gas:{align}}/{volume}')
print(f'{"~" * water_part:20}', f'{water:{align}}/{volume}')
