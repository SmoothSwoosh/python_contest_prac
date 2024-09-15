import math, itertools


#Проверка пересечения двух отрезков
#Код взят с geeksforgeeks
#Отсюда: https://www.geeksforgeeks.org/check-if-two-given-line-segments-intersect/
def onSegment(P, Q, R):
    (Px, Py), (Qx, Qy), (Rx, Ry) = P, Q, R
    return ((Qx <= max(Px, Rx)) and (Qx >= min(Px, Rx)) \
            and (Qy <= max(Py, Ry)) and (Qy >= min(Py, Ry)))

def orientation(P, Q, R):
    (Px, Py), (Qx, Qy), (Rx, Ry) = P, Q, R
    sign = (Qy - Py) * (Rx - Qx) - (Qx - Px) * (Ry - Qy)
    return 1 if sign > 0 else 2 if sign < 0 else 0

def doIntersect(p1, q1, p2, q2):
	o1 = orientation(p1, q1, p2)
	o2 = orientation(p1, q1, q2)
	o3 = orientation(p2, q2, p1)
	o4 = orientation(p2, q2, q1)

	if ((o1 != o2) and (o3 != o4)):
	    return True
	if ((o1 == 0) and onSegment(p1, p2, q1)):
	    return True
	if ((o2 == 0) and onSegment(p1, q2, q1)):
	    return True
	if ((o3 == 0) and onSegment(p2, p1, q2)):
	    return True
	if ((o4 == 0) and onSegment(p2, q1, q2)):
	    return True
	return False


#Это всё моё, родное
class Triangle:
    def __init__(self, *points):
        self.points = points

    def side_length(self, A, B):
        (x0, y0), (x1, y1) = A, B
        return math.hypot(x1 - x0, y1 - y0)

    def __bool__(self):
        return not math.isclose(0, abs(self), rel_tol=1e-3)

    def __abs__(self):
        A, B, C = self.points
        AB = self.side_length(A, B)
        BC = self.side_length(B, C)
        CA = self.side_length(C, A)
        
        s = (AB + BC + CA) / 2
        
        return (s * (s - AB) * (s - BC) * (s - CA)) ** 0.5
    
    def __lt__(self, other):
        return abs(self) < abs(other)

    def contains_point(self, point):
        """
        Производим триангуляцию из точек треугольника - A, B, C и проверяемой точки O
        Если сумма площадей полученных треугольников равна площади треугольника ABC,
        то точка O лежит внутри ABC
        """
        
        triangulation = 0
        for i in range(len(self.points)):
            triangulation += abs(Triangle(self.points[i], \
                                          self.points[(i+1)%len(self.points)], \
                                          point))
        
        return math.isclose(abs(self), triangulation, rel_tol=1e-3)
    
    def __contains__(self, other):
        """
        Если все точки одного треугольника находятся внутри другого,
        то первый треугольник целиком лежит внутри второго
        """
        
        return not other or all(self.contains_point(point) for point in other.points)

    def __and__(self, other):
        #Пустой треугольник, по условию, не пересекается ни с кем
        if not (other and self):
            return False

        #Если один из треугольников внутри другого, то они, очевидно, пересекаются
        if self in other or other in self:
            return True

        #Если хоть какие-то стороны треугольников пересекаются, значит, и треугольники пересекаются
        for first_side in itertools.combinations(self.points, 2):
            for second_side in itertools.combinations(other.points, 2):
                (p1, q1), (p2, q2) = first_side, second_side
                if doIntersect(p1, q1, p2, q2):
                    return True
        return False


r = Triangle((4, 2), (1, 3), (2, 4))
s = Triangle((1, 1), (3, 1), (2, 2))
t = Triangle((0, 0), (6, 0), (3, 5))
o = Triangle((0, 3), (6, 3), (3, -2))
print(*(f"{n}({bool(x)}):{round(abs(x), 3)}" for n, x in zip("rsto", (r, s, t, o))))
print(f"{s < t=}, {o < t=}, {r < t=}, {r < s=}")
print(f"{s in t=}, {o in t=}, {r in t=}")
print(f"{r & t=}, {t & r=}, {s & r=}, {o & t=}")
