def sloter(fields, default):
    class cls:
        __slots__ = fields

        def __init__(self):
            for field in self.__slots__:
                setattr(self, field, default)
                
        def __delattr__(self, field):
            setattr(self, field, default)
            
        def __iter__(self):
            return iter(getattr(self, field) for field in self.__slots__)
        
    return cls
