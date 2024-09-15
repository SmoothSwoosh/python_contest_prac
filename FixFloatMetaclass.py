import inspect
from functools import wraps
import numbers


def decorator(foo, ndigits):
    @wraps(foo)
    def wrapper(*args, **kwargs):
        res = foo(*args, **kwargs)
        if isinstance(res, numbers.Real):
            return round(res, ndigits)
        else:
            return res
    return wrapper


class fixed(type):
    def __new__(cls, clsname, bases, namespace, **kwds):
        ndigits = kwds['ndigits'] if 'ndigits' in kwds else 3
        
        for attr, value in namespace.items():
            if not inspect.ismethod(value) and inspect.isfunction(value):
                namespace[attr] = decorator(value, ndigits)
        return super().__new__(cls, clsname, bases, namespace)
