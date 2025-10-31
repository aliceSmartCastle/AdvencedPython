class tyingParameter:
    __slots__ = 'parameter'

    def __set_name__(self, owner, name):
        self.parameter = name

    def __get__(self, instance, owner):
        if instance is None:
            return self
        else:
            return instance.__dict__[self.parameter] or None