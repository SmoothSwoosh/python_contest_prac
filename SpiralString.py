class Spiral:
    def __init__(self, spiral):
        self.spiral = sorted(spiral, key=lambda char: spiral.index(char))

    def __iter__(self):
        return iter(self.spiral)

    def __str__(self):
        sum, side = 0, 0
        while sum < len(self.spiral):
            side += 1
            sum += side
            
        w, h = side * 2, side * 2
        canvas = [[' '] * w for i in range(h)]
        x, y = w // 2, h // 2

        x_up, y_up, x_down, y_down = x, y, x, y
        direction = 0
        step = 1
        k = 0
        while k < len(self.spiral):
            for i in range(step):
                if k >= len(self.spiral):
                    break
                canvas[y][x] = self.spiral[k]
                y_down = max(y_down, y)
                x_down = max(x, x_down)
                y_up = min(y_up, y)
                x_up = min(x_up, x)
                k += 1
                match direction:
                    case 0:
                        x += 1
                    case 1:
                        y -= 1
                    case 2:
                        x -= 1
                    case 3:
                        y += 1
            step += 1
            direction = (direction + 1) % 4

        ans = ''
        for i in range(y_up, y_down + 1):
            line = ''
            for j in range(x_up, x_down + 1):
                line += canvas[i][j]
            ans += line.rstrip()
            if i < y_down:
                ans += '\n'
        return ans

    def __add__(self, other):
        return Spiral(self.spiral + other.spiral)

    def __sub__(self, other):
        new_spiral = ''
        for char in set(self.spiral):
            if other.spiral.count(char) < self.spiral.count(char):
                new_spiral += char * (self.spiral.count(char) - other.spiral.count(char))

        new_spiral = sorted(new_spiral, key=lambda char: self.spiral.index(char))
        return Spiral(new_spiral)

    def __mul__(self, number):
        return Spiral(sorted(self.spiral * 2, key=lambda char: self.spiral.index(char)))
