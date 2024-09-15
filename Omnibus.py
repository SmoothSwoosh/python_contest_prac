class Omnibus:
    _attributes = {}

    def __delattr__(self, attr):
        if attr in self.__dict__:
            del self.__dict__[attr]
            Omnibus._attributes[attr] -= 1

    def __setattr__(self, attr, value):
        if not attr.startswith('_'):
            self.__dict__[attr] = 1
            Omnibus._attributes[attr] = Omnibus._attributes.get(attr, 0) + 1

    def __getattribute__(self, attr):
        return object.__getattribute__(self, attr) if attr not in Omnibus._attributes \
                                                   else Omnibus._attributes[attr]
