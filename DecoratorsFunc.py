import math
import os
from functools import wraps
from time import perf_counter
from typing import Any, Union, Callable, Dict

import psutil


def wrapperDetail(*args, **kwargs):
    """
     #TupleGenerics=TypeVar('TupleGenerics')\n
    param args:   Tuple[TupleGenerics]\n
    param kwargs: #**kwargs:Dict[Any,Any]\n
    return None
    """

    print(f"len:{len(args)}")
    for index, value in enumerate(range(len(args))):
        print(f"(index:{index},value:{value})")
    print(f"dictKey:{list(kwargs.keys())}")
    print(f"dictVal:{list(kwargs.values())}")


def CalculateAny(argument: Any) -> Any:
    # function document
    @wraps(argument)
    def wrapper(*args, **kwargs):
        #same to wrapperDetail document
        t1 = perf_counter()
        result = argument(*args, **kwargs)
        t0 = perf_counter()
        executeTime = t0 - t1
        print(f"the running  time is:{executeTime:6f} ms")
        print(type(argument))
        wrapperDetail(*args, **kwargs)
        return result

    return wrapper


#customer decorators for any function
@CalculateAny
def setterAngel(angel: Union[int, float], increaseAngel: int = 1) -> float:
    if not isinstance(increaseAngel, int):
        raise TypeError('the increaseAngel must be integer')

    # replace the lambda x:x+2
    def y(integer: int):
        return integer + 2

    return math.pow(math.cos(angel), y(integer=increaseAngel)) + math.pow(math.sin(angel), 2)


def GetterMemory() -> None:
    """
    this function output the ram memory using of system\n
    Argument:
           None
    return:
          None
    """
    ram = psutil.Process(os.getpid())
    print(f"the rss memory of system is :{ram.memory_info().rss / (math.pow(1024, 2)):4f}Mb")
    print(f"the vms memory of system is :{ram.memory_info().vms / (math.pow(1024, 2)):4f}Mb")


def ascii_dict() -> Dict[str, int]:
    chr_list = [chr(i) for i in range(65, 93)]
    inter_list = [i for i in range(65, 93)]
    asciiDict = {k: v for k, v in zip(chr_list, inter_list)}
    return asciiDict


def funcHelp(func: Callable[[...], None]):
    print('\n')
    help(func)
    print(f"the function name is:{func.__name__}")


def memoryHelp() -> None:
    funcHelp(memory_argumentInfo)


def repeat(times: int, loop: bool = False) -> Any:
    def decorators(func: Callable[[Any], Any]) -> Any:
        @wraps(func)
        def wrapper(*args, **kwargs) -> Any:
            global res
            print(type(func))
            wrapperDetail(*args, **kwargs)
            if loop:
                for _ in range(times):
                    res = func(*args, **kwargs)
            else:
                print(times * '*')
                res = func(*args, **kwargs)
                print(times * '*')
            return res

        return wrapper

    return decorators


def repeatString(strLike: str) -> str:
    return strLike


@repeat(times=3, loop=True)
def StringRepeat(strLink: str) -> None:
    print(f"the repeat string is:{repeatString(strLike=strLink)}")


class DecoratorClass:
    def __init__(self, times, loop: bool = False):
        self.StarTime = times
        self.loop = loop

    def __call__(self, func: Callable[[Any], Any]) -> Any:
        @wraps(func)
        def wrapper(*args, **kwargs) -> Any:
            global funcResult
            print(type(self.StarTime))
            wrapperDetail(*args, **kwargs)
            if self.loop:
                for _ in range(self.StarTime):
                    funcResult = func(*args, **kwargs)
            else:
                print(self.StarTime * '*')
                funcResult = func(*args, **kwargs)
                print(self.StarTime * '*')
            return funcResult

        return wrapper


@DecoratorClass(times=35)
def AsciiInfo() -> None:
    """
    it's split of big ascii dictionary
    to small dictionary,every small dictionary has 4 keys and values
    make it to tuple,finally pretty print it
    """
    integerList = list(ascii_dict().values())
    AlphaList = list(ascii_dict().keys())

    tupleAscii = (dict(zip(AlphaList[0:4], integerList[0:4])), dict(zip(AlphaList[4:8], integerList[4:8])),
                  dict(zip(AlphaList[8:12], integerList[8:12])), dict(zip(AlphaList[12:16], integerList[12:16])),
                  dict(zip(AlphaList[16:20], integerList[16:20])), dict(zip(AlphaList[20:24], integerList[20:24])),
                  dict(zip(AlphaList[24:28], integerList[24:28]))

                  )
    for i in range(len(tupleAscii)):
        print(tupleAscii[i])


def easyAdd(a: Union[float, int], b: Union[float, int]) -> float:
    return a + b


def RepeatApp(a: Union[float, int], b: Union[float, int]) -> None:
    numberRes = DecoratorClass(times=28)(easyAdd)
    print(f"the riddle method result is:{numberRes(a, b)}")


def JojoSay(cls: Any) -> Any:
    cls.say = lambda self, message: print(message)
    return cls


@JojoSay
class Speak:
    def __init__(self, saying: str):
        self.speech = saying

    def say(self, param: str) -> None:
        pass


if __name__ == "__main__":
    print('-' * 12 + "using decorators" + '-' * 12)
    angels = CalculateAny(setterAngel)
    print(f"the angel res is:{setterAngel(angel=10.2, increaseAngel=2):.4f}")
    print('-' * 12 + "using the functions" + '-' * 12)
    memory_argumentInfo = CalculateAny(GetterMemory)
    memory_argumentInfo()
    print('-' * 12 + 'decorator with arguments' + '-' * 12)
    StringRepeat(strLink="roland")
    print('-' * 12 + 'decorator with class' + '-' * 12)
    AsciiInfo()
    RepeatApp(a=1, b=8)
    print('-' * 12 + 'monkey-patching' + '-' * 12)
    JoeStar = Speak("joseph joeStar")
    JoeStar.say('Zeppelin is my best friend')
