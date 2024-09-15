import collections, sys


class DivStr(collections.UserString):
    def __init__(self, string=''):
        super().__init__(string)

    def __mod__(self, n):
        return self[-(len(self)%n):]
    
    def __floordiv__(self, n):
        length = len(self) // n
        if length == 0:
            return ''
        
        return iter([self[i:i+length] for i in range(0, len(self), length)])


exec(sys.stdin.read())
