class NegExt:
    def __neg__(self):
        try:
            return type(self)(super().__neg__())
        except AttributeError:
            try:
                return type(self)(super().__getitem__(slice(1, -1)))
            except Exception:
                return type(self)(self)
