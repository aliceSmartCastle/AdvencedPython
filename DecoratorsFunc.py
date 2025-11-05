import math
import os
from functools import wraps
from itertools import chain
from time import perf_counter
from typing import Any, Union, Callable, Dict

import psutil


def wrapperDetail(*args, **kwargs) -> Dict[str, Any]:
    """
     #TupleGenerics=TypeVar('TupleGenerics')\n
    param args:   Tuple[TupleGenerics]\n
    param kwargs: #**kwargs:Dict[Any,Any]\n
    return dict
    *:arg[0] maybe is the class,so I will initial to it,and on so,it has __dict__
    """
    index_list = []
    args_list = []
    for index, value in enumerate(range(len(args))):
        index_list.append(index)
        if len(args) == 1:
            #class is first argument
            cls = args[value]
            args_list.append(cls.__dict__)
            #args[value] is the class
        else:
            args_list.extend(args[value])
    return {"argLen": len(args), 'dictKey': tuple(kwargs.keys()), 'dictVal': tuple(kwargs.values()),
            'argIndex': tuple(index_list), 'argVal': tuple(args_list)}


def CalculateAny(argument: Any) -> Any:
    # function document
    @wraps(argument)
    def wrapper(*args, **kwargs):
        #same to wrapperDetail document
        t1 = perf_counter()
        result = argument(*args, **kwargs)
        t0 = perf_counter()
        executeTime = t0 - t1
        print(f"the running time is:{executeTime:6f} ms")
        # print(f"argument type is :{type(argument)}")
        # default always is function type
        print(f"the function dictionary is :{wrapperDetail(*args, **kwargs)}")
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


def funcHelp(func: Callable[[None], None]):
    print('\n')
    help(func)
    print(f"the function name is:{func.__name__}")


def memoryHelp(memory_argumentInfo=None) -> None:
    if memory_argumentInfo is None:
        memory_argumentInfo = 0
    funcHelp(memory_argumentInfo)


def spiteLine(*, context: str = '', symbol: str = '*', counter: int = 12) -> str:
    return ''.join([symbol * counter, context, symbol * counter])


def repeat(times: int, loop: bool = False) -> Any:
    def decorators(func: Callable[[Any], Any]) -> Any:
        @wraps(func)
        def wrapper(*args, **kwargs) -> Any:
            funcRes = None
            print(type(func))
            wrapperDetail(*args, **kwargs)
            if loop:
                for _ in range(times):
                    res = func(*args, **kwargs)
                    funcRes = res
            else:
                print(times * '*')
                funcRes = func(*args, **kwargs)
                print(times * '*')
            return funcRes

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

    def __call__(self, func: Any) -> Any:
        @wraps(func)
        def wrapper(*args, **kwargs) -> Any:
            funcResult = None
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


def flatten(nested_list):
    result_list = []
    for item in nested_list:
        if isinstance(item, list):
            result_list.extend(flatten(item))
        else:
            result_list.append(item)
    return result_list


def flatten_res(nested_list: list):
    return list(chain.from_iterable(
        [flatten([nested_list]) if isinstance(nested_list, list) else [item_list] for item_list in nested_list]))
