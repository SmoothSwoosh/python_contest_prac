class Pushpull:
    position = 0
    
    def __init__(self, pos=0):
        Pushpull.position = pos

    def __iter__(self):
        step = 1 if self.position > 0 else -1
        return iter(range(0, self.position, step))

    def __str__(self):
        if self.position < 0:
            return f'<{-self.position}<'
        elif self.position > 0:
            return f'>{self.position}>'
        else:
            return f'<0>'
        
    def push(self, n=1):
        Pushpull.position += n

    def pull(self, n=1):
        Pushpull.position -= n
