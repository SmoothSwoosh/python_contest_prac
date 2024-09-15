import sys


class Num:
    def __set__(self, obj, value):
        if hasattr(value, 'real'):
            obj._num = value
        else:
            obj._num = len(value)

    def __get__(self, obj, cls):
        if hasattr(obj, '_num'):
            return obj._num
        else:
            return 0

    def __delete__(self, obj):
        del obj._num


exec(sys.stdin.read())
