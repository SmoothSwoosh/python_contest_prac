import sys


def objcount(cls):
    class rapper:
        counter = 0
        
        def __init__(self):
            super().__init__()
            type(self).counter += 1

        def __del__(self):
            type(self).counter -= 1
            try:
                super().__del__()
            except:
                pass

    return rapper


exec(sys.stdin.read())
