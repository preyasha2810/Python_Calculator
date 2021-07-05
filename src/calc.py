from Add import Addition
from Sub import Subtraction
from Mult import Multiplication
from Div import Division
from Square import Square
from SquareRoot import SquareRoot


class Calc:
    result = 0

    def __init__(self):
        self.result = 0

    def add(self, a, b):
        self.result = Addition.Add(a, b)
        return self.result

    def subtract(self, a, b):
        self.result = Subtraction.Sub(a, b)
        return self.result

    def divide(self, a, b):
        self.result = Division.Div(a, b)
        return self.result

    def multiply(self, a, b):
        self.result = Multiplication.Mult(a, b)
        return self.result

    def square(self, a):
        self.result = Square.Square(a)
        return self.result

    def squareroot(self, a):
        self.result = SquareRoot.SquareRoot(a)
        return self.result
