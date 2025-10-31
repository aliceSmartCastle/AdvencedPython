from dataclasses import dataclass
from tyingCheck import tyingParameter


class IntegerValue(tyingParameter):

    def __set__(self, instance, value):
        if not isinstance(value, int):
            raise TypeError("value must the integer") from None
        else:
            instance.__dict__[self.parameter] = value
            return value


@dataclass
class WatchRefence:
    integerData: int = IntegerValue()

    def __post_init__(self):
        ...

    def __str__(self):
        return f"the integer value is :{self.integerData}"

    def HiddenId(self):
        return hex(id(self.integerData))

    def strId(self):
        return f"the id of the object is :{self.HiddenId()}"


if __name__ == "__main__":
    alpha = WatchRefence(12)
    print(alpha, alpha.strId(), sep='\n')
    alpha.integerData = 300
    print(alpha, alpha.strId(), sep='\n')
