import inspect
import types
import typing


class init(type):    
    def __init__(cls, clsname, bases, namespace, **kwds):
        new_namespace = namespace.copy()
        for attr, value in namespace.items():
            if not inspect.ismethod(value) and inspect.isfunction(value):
                sig = inspect.signature(value)
                annotation = inspect.get_annotations(value)


                new_defaults = []
                for param, ann in sig.parameters.items():
                    if param in annotation and ann.default is ann.empty:
                        param_type = annotation[param]

                        if isinstance(param_type, types.GenericAlias):
                            new_defaults.append(typing.get_origin(param_type)())
                        else:
                            try:
                                new_defaults.append(param_type())
                            except:
                                new_defaults.append(None)
                                
                value.__defaults__ = tuple(new_defaults) + (value.__defaults__ or ())

        return super().__init__(clsname, bases, namespace)
