def turtle(coord, course):
    (x, y), direction = coord, course
    direction = {0:'e', 1:'n', 2:'w', 3:'s'} [direction]
    compass = ['s', 'w', 'n', 'e'] #south, west, north, east
    moves = {'s':(0, -1), 'w':(-1, 0), 'n':(0, 1), 'e': (1, 0)}

    step = yield (x, y)
    while step:
        if step == 'l':
            direction = compass[compass.index(direction) - 1]
        elif step == 'r':
            direction = compass[(compass.index(direction) + 1) % len(compass)]
        else:
            x += moves[direction][0]
            y += moves[direction][1]
        step = yield (x, y)
