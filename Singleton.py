class final(type):
    def __new__(metacls, name, parents, namespace):
        for cls in parents:
            if isinstance(cls, final):
                raise TypeError(f"{cls.__name__} is final")
        return super().__new__(metacls, name, parents, namespace)


class Singleton(type):
    _instance = None
    def __call__(cls, *args, **kw):
        if cls._instance is None:
             cls._instance = super().__call__(*args, **kw)
        return cls._instance


class Both(type):
	def __init__(self, single: None, fin: None):
		if fin:
			def __new__(metacls, name, parents, namespace):
	        for cls in parents:
	            if isinstance(cls, final):
	                raise TypeError(f"{cls.__name__} is final")
	        return super().__new__(metacls, name, parents, namespace)
	     	self.__new__ = new 
	     if single:
	     	_instance = None
		    def call(cls, *args, **kw):
		        if cls._instance is None:
		             cls._instance = super().__call__(*args, **kw)
		        return cls._instance
		    self.__call__ = call 