import math


class InvalidInput(Exception): pass
class BadTriangle(Exception): pass


def triangle_square(inStr):
    try:
        (x1, y1), (x2, y2), (x3, y3) = eval(inStr)
    except:
        raise InvalidInput

    if not all(isinstance(coord, (int, float)) \
               for coord in [x1, y1, x2, y2, x3, y3]):
        raise BadTriangle

    side_length = lambda x0, y0, x1, y1: math.hypot(x1 - x0, y1 - y0)
    AB = side_length(x1, y1, x2, y2)
    BC = side_length(x2, y2, x3, y3)
    CA = side_length(x3, y3, x1, y1)

    if not (AB + BC > CA and AB + CA > BC and CA + BC > AB):
        raise BadTriangle

    s = (AB + BC + CA) / 2
    area = (s * (s - AB) * (s - BC) * (s - CA)) ** 0.5

    if area < 1e-2:
        raise BadTriangle
    
    return area
    

while inStr := input():
    try:
        area = triangle_square(inStr)
    except InvalidInput:
        print('Invalid input')
    except BadTriangle:
        print('Not a triangle')
    else:
        print('%.2f' % area)
