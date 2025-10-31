import copy
from dataclasses import dataclass
from enum import Enum, auto

from tyingCheck import tyingParameter


class ParameterName(Enum):
    alpha = auto()
    beta = auto()
    gamma = auto()


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
        return f"the id of the object is :{self.HiddenId()}"  # memory address

    def __copy__(self):  #Shallow Copy
        return WatchRefence(self.integerData)

    def __deepcopy__(self, memo):
        return WatchRefence(copy.deepcopy(self.integerData, memo))

    def parameterTuple(self, EnumName):
        return tuple([EnumName, self.integerData, self.HiddenId()])


if __name__ == "__main__":
    alpha = WatchRefence(12)
    print(alpha.parameterTuple(ParameterName.alpha.name))
    alpha.integerData = 300
    print(alpha.parameterTuple(ParameterName.alpha.name))
    beta = copy.copy(alpha)                              #beta is reference of alpha
    print(beta.parameterTuple(ParameterName.beta.name))
    gamma = copy.deepcopy(alpha)
    print(gamma.parameterTuple(ParameterName.gamma.name))
    print(gamma.parameterTuple(ParameterName.gamma.name)[2] == beta.parameterTuple(ParameterName.beta.name)[2])
