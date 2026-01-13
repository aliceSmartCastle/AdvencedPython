import cmath
import math
from dataclasses import dataclass



@dataclass
class Equation:
    __expression: str
    __mathSymbol: str
    __last      : str = None


    def __post_init__(self):

        if '(' not in self.left_expression() and len(self.solution_init()) == 2:
         self.expreess_middle()
        if len(self.solution_init()) == 1:
            print(f"the function {self.__expression}\nis not solve")
            return None
        elif len(self.solution_init()) == 2:
            return  None
        if self.__mathSymbol not in self.__expression:
            raise ValueError('Invalid math symbol')
        return None

    @staticmethod
    def formula(a =0 , b =0, c =0):
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

    def left_expression(self):
        return self.__expression.split('=')[1]

    def expression_post(self):
        first_stage = self.left_expression().split('²')[0]
        first_stage.startswith('-')
        if first_stage.startswith('-'):
            return self.left_expression()
        else:
            return '+' + self.left_expression()

    def solution_init(self):
        symbolList = []
        for i in range(len(self.expression_post())):
            if self.expression_post()[i].isalnum():
                pass
            else:
                symbolList.append(self.expression_post()[i])
        return symbolList

    def empty_expression(self, expression, argument):

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

    def head_expression(self):


        if self.solution_init() == ['-','-','-']:
            head_pass = self.expression_post().split('²')
            return int(head_pass[0].split(self.__mathSymbol)[0])
        elif self.solution_init() == ['+', '-', '-']:
            return int(self.expression_post().split(self.__mathSymbol)[0])

        else:
            split_expression = self.expression_post().split('+')
            headStart, *headMiddle, test = split_expression
            return self.empty_expression(split_expression, headStart)

    def expreess_middle(self):

        if self.solution_init() != ['-','-','-']:
         start,*middle,self.__last = self.expression_post().split('+')
         if len(middle) == 1 and self.solution_init() == ['+', '-', '+']:
             return middle[0].split(self.__mathSymbol)[1].split('²')[1]
         elif len(middle) == 2:
             return int(middle[1].split(self.__mathSymbol)[0])
         elif self.solution_init() == ['+', '-', '-']:
             return int(self.__last.split(self.__mathSymbol)[1])
         elif self.solution_init() == ['-', '-', '+']:
             return start.split(self.__mathSymbol)[1].split('²')[1]
         elif self.solution_init() == ['-', '+', '+']:
             return middle[0].split(self.__mathSymbol)[0]
         else:
             return int(self.__last.split(self.__mathSymbol)[0])
        else:
            _, *middle, self.__last = self.expression_post().split(self.__mathSymbol)
            return int(middle[0].split('²')[1])



    def parse_need(self,expression):
        if self.__mathSymbol in expression:
            if len(expression.split(self.__mathSymbol)) == 2 :
             return int(expression.split(self.__mathSymbol)[1])
            elif len(expression.split(self.__mathSymbol)) == 3:
                return int(expression.split(self.__mathSymbol)[2])
            else:
                raise ValueError('Invalid math value')

        else:
            return ''



    def expreess_end(self):
         if self.parse_need(self.__last):
          return self.parse_need(self.__last)
         else:
          return self.__last
    def string_result(self,x1,x2):
      if x1 == 0 or x2 == 0:
          return f"the function {self.__expression}\ncan not be solved\n"
      return (f"the function {self.__expression}\n"
              f"has two root\n"
              f"x1 = {x1}\n"
              f"x2 = {x2}\n")

    def solve_spical(self,expression):



        if len(expression) == 2:
            print(self.string_result(expression[0],expression[1]))
            return None
        elif len(expression) == 3:
            if expression[0] == '-':
                print(self.string_result(-int(expression[0]+expression[1]),-int(expression[2])))
                return None
            else:
                print(self.string_result(-int(expression[0]),-int(expression[1]+expression[2])))
                return None
        elif len(expression) == 4 :
            print(self.string_result(-int(expression[0] + expression[1]), -int(expression[2] + expression[3])))
            return None
        else:
            return 'no realize method'

    def spical_expression(self):
        number_list=[]
        if self.left_expression().split('(')[1].startswith('x') and self.left_expression().split('(')[2].startswith('x'):
            for i in range(len(self.left_expression())):
                if self.left_expression()[i].isdigit():
                    number_list.append(self.left_expression()[i])
                elif '-' in self.left_expression()[i]:
                    number_list.append((self.left_expression()[i]))
        self.solve_spical(number_list)




    def solve(self):


        if '(' not in self.left_expression() and len(self.solution_init()) == 3:
          x1,x2 = self.formula(self.head_expression(),int(self.expreess_middle()),self.expreess_end())
          print(self.string_result(x1,x2))
        elif len(self.solution_init()) == 1:
            pass
        elif len(self.solution_init()) == 2:
            print(self.head_expression())
            pass
        else:
            self.spical_expression()

def main():

    questions = Equation('f(x)=2x²+9x+10', 'x')
    questions.solve()


if __name__ == '__main__':
    main()
