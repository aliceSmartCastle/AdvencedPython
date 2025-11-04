import math
from collections import namedtuple
from functools import lru_cache
from typing import Any
from DecoratorsFunc import CalculateAny


class Point2D:
    def __init__(self, xCoord, yCoord):
        self.x = xCoord
        self.y = yCoord

    def __eq__(self, other):
        if isinstance(other, Point2D):
            return (self.x == other.x) and (self.y == other.y)
        return False

    def __str__(self):
        return f"point:({self.x},{self.y})"

    def __hash__(self):
        return hash(min(self.x, self.y))

    @CalculateAny
    def maxSubList(self) -> None:
        subList = [round(1 / self.x + (math.sqrt(j * self.y)), 4) for j in range(2, 100)]
        print(f"max result of this list is :{max(subList)}")


@CalculateAny
def makeNameTuple(*args):
    Point2Ds = namedtuple(*args, rename=True)
    return Point2Ds


def listTuples() -> Any:
    return makeNameTuple("Point2D", ['x', 'y', 'x'])


def tupleNested() -> Any:
    return makeNameTuple("Point2D", ("x", "y"))


def commonTuples() -> Any:
    return makeNameTuple("Point2D", "x , y")


def stringTuples() -> Any:
    return makeNameTuple("Point2D", "x y")


def instanceTuples(argTuple):
    if isinstance(argTuple, listTuple):
        print("the nameTuple is same of the listTuple ")
    if isinstance(argTuple, tuple):
        print("the nameTuple is same of the tuple")


@lru_cache
def splitLine(context: str) -> None:
    print(12 * '*' + context + 12 * '*')


if __name__ == "__main__":
    splitLine("using Point2d class")
    pointX = Point2D(3, 4)
    pointY = Point2D(3, 4)
    pointX.maxSubList()
    print(pointX == pointY)
    print(pointX is pointY)
    pointSet = {pointX, pointY}
    splitLine('using nameTuple')
    listTuple = listTuples()
    TupleInstant = listTuple(12, 15, 20)
    nesteTuple = tupleNested()
    nestedVal: Any = nesteTuple(x=100, y=50)
    splitLine('instantiation of namedtuple')
    instanceTuples(TupleInstant)
    splitLine('unpacking namedtuple')
    cordX, coordY, noValid = TupleInstant
    print(f"Point2D:({cordX},{coordY})")
    splitLine('using index and iterating')
    for i in range(len(nestedVal)):
        print(f"index:{i} value:{TupleInstant[i]}")
    print(TupleInstant._fields)
    splitLine('using Additional attributes')
    listTupCopy: Any = listTuple(12, 15, 20)
    print(listTupCopy == TupleInstant)
    #__eq__
    print(nestedVal)
    #__str__
    print(f"the max value is:{max(nestedVal)}\nthe min value is:{min(nestedVal)}")
    #__lt__,__gt__
    listPoints = list(pointSet)
    for i in range(len(listPoints)):
        print(listPoints[i])
