class alias:

    def __init__(self, name, write=False):
        self.name, self.write = name, write

    def __get__(self, instance, owner):
        if instance is None:
            return getattr(owner, self.name)
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        if self.write:
            setattr(instance, self.name, value)
        else:
            raise AttributeError()
