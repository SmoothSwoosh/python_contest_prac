import math, sys


class Grange:
    def __init__(self, *args):
        self.b0, self.q, self.bound = args

    def __iter__(self):
        return (self.b0 * self.q ** n for n in range(len(self)))

    def __str__(self):
        return f'grange({self.b0}, {self.q}, {self.bound})'

    def __repr__(self):
        return f'grange({self.b0}, {self.q}, {self.bound})'

    def __len__(self):
        return math.ceil(math.log(self.bound / self.b0, self.q))

    def __getitem__(self, key):
        if isinstance(key, slice):
            start, stop, step = key.start, key.stop, key.step if key.step else 1
            return Grange(start, self.q ** step, stop)
        else:
            return self.b0 * self.q ** key

exec(sys.stdin.read())
