import sys


def method(foo):
    def output(*args, **kwargs):
        print(f'{foo.__name__}: {args[1:]}, {kwargs}')
        return foo(*args, **kwargs)
    return output


class dump(type):
    def __new__(metacls, name, parents, namespace, **kwords):
        cls = super().__new__(metacls, name, parents, namespace)
        for attr, value in namespace.items():
            setattr(cls, attr, method(value) if callable(value) \
                                            else value)

        return cls                   


exec(sys.stdin.read())
