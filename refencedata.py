import copy
import ctypes
import gc
import math
import os
from dataclasses import dataclass
from enum import Enum, auto
from typing import Union
import psutil

from tyingCheck import tyingParameter


class ParameterName(Enum):
    alpha = auto()
    beta = auto()
    gamma = auto()


class IntegerValue(tyingParameter):

    def __set__(self, instance, value):
        if value is None:
            return None
        if isinstance(value, int):
            instance.__dict__[self.parameter] = value
            return value
        else:
            raise TypeError("value must the integer") from None


@dataclass
class WatchRefence:
    integerData: Union[int, IntegerValue] = IntegerValue()

    @staticmethod
    def __post_init__():
        ...

    def __str__(self):
        return f"the integer value is :{self.integerData}"

    def HiddenId(self):
        return hex(id(self.integerData))

    def strId(self):
        return f"the id of the object is :{self.HiddenId()}"  # memory address

    def __copy__(self):
        return WatchRefence(self.integerData)  #Shallow Copy

    def __deepcopy__(self, memo):
        return WatchRefence(copy.deepcopy(self.integerData, memo))

    def parameterTuple(self, EnumName: ParameterName) -> tuple:
        return tuple([EnumName.name, self.integerData, self.HiddenId()])

    def AddressSame(self, other) -> None:
        if self.HiddenId() == other.HiddenId():
            print("this the same memery address")
        else:
            print("not in the same memary address")

    def GetId(self) -> int:
        return id(self)

    @staticmethod
    def refenceCounter(address: int) -> int:
        return ctypes.c_long.from_address(address).value

    @staticmethod
    def OutCount(objectId: int) -> None:
        print(f"the value refence count is :{WatchRefence.refenceCounter(objectId)}")

    @staticmethod
    def ObjectExit(objectId: int) -> bool:
        for obj in gc.get_objects():
            if id(obj) == objectId:
                return True
        else:
            return False


if __name__ == "__main__":
    alpha = WatchRefence(12)
    alphaData = alpha.parameterTuple(ParameterName.alpha)
    beta = copy.copy(alpha)
    #beta is reference of alpha
    betaData = beta.parameterTuple(ParameterName.beta)
    gamma = copy.deepcopy(alpha)
    gammaData = gamma.parameterTuple(ParameterName.gamma)
    beta.AddressSame(gamma)
    alpha.integerData = 300  #change the integerData value to 300,so it memery address is not same to initial
    ParseAlpha = alpha.parameterTuple(ParameterName.alpha)
    #refence counter block
    VarRef = alpha.GetId()
    betaRef = beta.GetId()
    print(f"beta is exit? {WatchRefence.ObjectExit(betaRef)}")
    AlphaRef = alpha  #refence value,not copy or deepcopy
    refenceAlpha = AlphaRef.parameterTuple(ParameterName.alpha)
    print(f"alpha is exit?{WatchRefence.ObjectExit(VarRef)}")
    WatchRefence.OutCount(VarRef)  #2
    del alpha
    WatchRefence.OutCount(VarRef)  #1
    del AlphaRef
    WatchRefence.OutCount(VarRef)  #0
    addressList = [alphaData, betaData, gammaData, ParseAlpha, refenceAlpha]

    print(f"alpha is exit?{WatchRefence.ObjectExit(VarRef)}")
    del beta
    print(f"beta is exit? {WatchRefence.ObjectExit(betaRef)}")
    for i in addressList:
        print(i)
    print(os.name)
    processMemory = psutil.Process(os.getpid())
    print(f"rss memory is {processMemory.memory_info().rss / (math.pow(1024, 2)):4f} Mb")
    print(f"vms memory is {processMemory.memory_info().vms / (math.pow(1024, 2)):4f} Mb")
