import types
import typing
import inspect
import sys


class check(type):
    def __new__(metacls, clsname, bases, namespace, **kwds):
        def sub_check(cls, attr, origin):
            origin = origin.__origin__ if isinstance(origin, types.GenericAlias)\
                                     else origin

            return hasattr(cls, attr) and isinstance(getattr(cls, attr), origin)
                
        
        def check_annotations(self):
            annotation = inspect.get_annotations(self.__class__)

            return all(sub_check(self, attr, value) for attr, value in annotation.items()\
                                               if not callable(attr))


        namespace['check_annotations'] = check_annotations


        return super().__new__(metacls, clsname, bases, namespace)


exec(sys.stdin.read())
