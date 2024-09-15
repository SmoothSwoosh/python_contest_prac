import sys


class Alpha:
    __slots__ = [chr(a) for a in range(ord('a'), ord('z') + 1)]

    def __init__(self, *args, **kwargs):
        for attr, value in kwargs.items():
            setattr(self, attr, value)

    def __str__(self):
        notation = ''
        for attr in self.__slots__:
            if hasattr(self, attr):
                notation += '{}: {}, '.format(attr, getattr(self, attr))

        return notation[:-2]


class AlphaQ:
    _fields = {}
    _legal_fields = [chr(a) for a in range(ord('a'), ord('z') + 1)]
    
    def __init__(self, *args, **kwargs):
        for attr, value in kwargs.items():
            setattr(self, attr, value)

    def __setattr__(self, attr, value):
        if attr in self._legal_fields:
            self._fields[attr] = value
        else:
            raise AttributeError

    def __getattr__(self, attr):
        if attr in self._fields:
            return self._fields[attr]
        else:
            raise AttributeError

    def __str__(self):
        sorted_fields = {key: self._fields[key] for key in sorted(self._fields)}
        return ', '.join(f'{key}: {value}' for key, value in sorted_fields.items())


exec(sys.stdin.read())
