def fix(n):
    def decorator(fun):
        def newfun(*args, **kwargs):
            args = [round(arg, n) if isinstance(arg, float) else arg\
                                    for arg in args]

            kwargs = {key:round(value, n) if isinstance(value, float) else value\
                                          for key, value in kwargs.items()}

            res = fun(*args, **kwargs)
            return round(res, n) if isinstance(res, float) else res
        return newfun
    return decorator
