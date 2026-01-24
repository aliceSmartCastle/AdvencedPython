import cmath
import math
from dataclasses import dataclass
from typing import Any


@dataclass
class Equation:
    __expression: str
    __mathSymbol: str
    __power: str
    __last: str|None = None
    x1 :float |None = None
    x2 :float |None = None


    def __post_init__(self):
        if not self.__expression.strip().startswith('f(x)'):
            raise ValueError('Invalid expression')
        elif self.__mathSymbol not in self.__expression:
            raise ValueError('Invalid math symbol')
        elif '.' in self.__expression:
            raise ValueError('Invalid expression')
        if '(' not in self.left_expression() and len(self.solution_init()) == 3:
            pass
        if len(self.solution_init()) == 1:
            print(f"the function {self.__expression}\nis not solve")
        elif len(self.solution_init()) == 2:
           pass


    @staticmethod
    def formula(a: str|int = 0, b: str|int = 0, c: str|int = 0) -> tuple[complex, complex] | tuple[float, float]:
        metaAlfa = int(a)
        metaBeta = int(b)
        metaGamma = int(c)

        condition = math.pow(metaBeta, 2) - 4 * metaAlfa * metaGamma

        if condition <= 0:
            x1 = (-metaBeta + cmath.sqrt(condition)) / (2 * metaAlfa)
            x2 = (-metaBeta - cmath.sqrt(condition)) / (2 * metaAlfa)
            return x1, x2
        else:
            x1 = (-metaBeta + math.sqrt(condition)) / (2 * metaAlfa)
            x2 = (-metaBeta - math.sqrt(condition)) / (2 * metaAlfa)
            return x1, x2

    def left_expression(self) -> str:
        return self.__expression.split('=')[1]

    def expression_post(self) -> str:
        first_stage = self.left_expression().split(self.__power)[0]
        if first_stage.startswith('-'):
            return self.left_expression()
        else:
            return '+' + self.left_expression()

    def solution_init(self) -> list[Any]:
        symbolList = []
        for i in range(len(self.expression_post())):
            if self.expression_post()[i].isalnum():
                pass
            else:
                symbolList.append(self.expression_post()[i])
        return symbolList

    def empty_expression(self, expression: list[str], argument: str) -> int | str:

        if argument:
            if expression[0].split(self.__mathSymbol)[0] == '-':
                return -1
            else:
                return expression[0].split(self.__mathSymbol)[0]
        else:
            expression.pop(0)
            exprFirst, *_, _ = expression
            if exprFirst:
                if exprFirst.startswith(self.__mathSymbol):
                    return 1
                else:
                    return exprFirst.split(self.__mathSymbol)[0]
            else:
                raise ValueError('Invalid math symbol')

    def head_expression(self) -> str:

        if self.solution_init() == ['-', '-', '-']:
            head_pass = self.expression_post().split('²')
            return head_pass[0].split(self.__mathSymbol)[0]
        elif self.solution_init() == ['+', '-', '-']:
            return self.expression_post().split(self.__mathSymbol)[0]

        else:
            split_expression = self.expression_post().split('+')
            headStart, *headMiddle, test = split_expression
            return self.empty_expression(split_expression, headStart)

    def express_middle(self) -> str:
        if self.solution_init() != ['-', '-', '-']:
            start, *middle, self.__last = self.expression_post().split('+')
            if len(middle) == 1 and self.solution_init() == ['+', '-', '+']:
                return middle[0].split(self.__mathSymbol)[1].split('²')[1]
            elif len(middle) == 2:
                return middle[1].split(self.__mathSymbol)[0]
            elif self.solution_init() == ['+', '-', '-']:
                return self.__last.split(self.__mathSymbol)[1].split(self.__power)[1]
            elif self.solution_init() == ['-', '-', '+']:
                return start.split(self.__mathSymbol)[1].split(self.__power)[1]
            elif self.solution_init() == ['-', '+', '+']:
                return middle[0].split(self.__mathSymbol)[0]
            else:
                return self.__last.split(self.__mathSymbol)[0]
        else:
            start, *middle, self.__last = self.expression_post().split('-')
            number_mid = middle[1].split(self.__mathSymbol)
            return '-' + number_mid[0]

    def parse_need(self, expression) -> str | None:
        if self.__mathSymbol in expression:
            if len(expression.split(self.__mathSymbol)) == 2:
                return expression.split(self.__mathSymbol)[1]
            elif len(expression.split(self.__mathSymbol)) == 3:
                return expression.split(self.__mathSymbol)[2]
            else:
                raise ValueError('Invalid math value')

        else:
            return ''

    def expreess_end(self) -> str:
        if self.parse_need(self.__last):
            return self.parse_need(self.__last)
        else:
            if self.solution_init() == ['-', '-', '-']:
                return '-' + self.__last
            else:
                return self.__last

    def string_result(self, x1:float, x2:float) -> str:
        if x1 == 0 or x2 == 0:
            return f"the function {self.__expression}\ncan not be solved\n"
        self.x1=x1
        self.x2=x2


        return (f"the function {self.__expression.strip()}\n"
                f"has two root\n"
                f"x1 = {x1}\n"
                f"x2 = {x2}\n")
    def solve_spical(self, expression: list[Any]) -> str | None:

        if len(expression) == 2:
            print(self.string_result(expression[0], expression[1]))
            return None
        elif len(expression) == 3:
            if expression[0] == '-':
                print(self.string_result(-int(expression[0] + expression[1]), -int(expression[2])))
                return None
            else:
                print(self.string_result(-int(expression[0]), -int(expression[1] + expression[2])))
                return None
        elif len(expression) == 4:
            print(self.string_result(-int(expression[0] + expression[1]), -int(expression[2] + expression[3])))
            return None
        else:
            return 'no realize method'

    def spical_expression(self) -> str | None:
        number_list = []
        assert len(self.left_expression()) >= 2, 'the expression split length is less than 2'
        if self.left_expression().split('(')[1].startswith(self.__mathSymbol) and self.left_expression().split('(')[2].startswith(
                self.__mathSymbol):
            for i in range(len(self.left_expression())):
                if self.left_expression()[i].isdigit():
                    number_list.append(self.left_expression()[i])
                elif '-' in self.left_expression()[i]:
                    number_list.append((self.left_expression()[i]))
        self.solve_spical(number_list)
    def specially_head(self,expr:str) -> int:
        if expr =='+x':
            return 1
        elif expr == '-x':
            return -1
        else:
         return int(expr.split(self.__mathSymbol)[0])
    def specially_middle(self,expr:str) -> int:
        return int(expr.split(self.__mathSymbol)[0])
    def specially_end(self,expr:str) -> int:
        return int(expr.split(self.__mathSymbol)[0])

    def especially_expression(self, expr: list[str]) ->  None:
        assert len(expr) >= 2
        if self.__mathSymbol in expr[1]:
           x1,x2 = self.formula(a=self.specially_head(expr[0]),b=self.specially_middle(expr[1])) #ax²+bx
           print(self.string_result(x1,x2))
        else:
            x1,x2 = self.formula(a=self.specially_head(expr[0]),c=self.specially_end(expr[1]))
            print(self.string_result(x1,x2))

    def solve(self) -> None:

        if '(' not in self.left_expression() and len(self.solution_init()) == 3:
            x1, x2 = self.formula(self.head_expression(), (self.express_middle()), self.expreess_end())
            print(self.string_result(x1, x2))
            return None
        elif len(self.solution_init()) == 1:
            return None
        elif len(self.solution_init()) == 2:
            self.especially_expression(self.expression_post().split(self.__power))
            return None
        else:
            self.spical_expression()
            return None


def main():

    expr = Equation('f(x)=2x²+6x-12', 'x', '²')
    expr.solve()



if __name__ == '__main__':
    main()
