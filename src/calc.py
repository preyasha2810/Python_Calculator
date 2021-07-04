import math


def addition(a, b):
    return int(a) + int(b)


def subtraction(a, b):
    return int(a) - int(b)


def division(a, b):
    if int(b) != 0:
        return float(a) / float(b)
    else:
        return ZeroDivisionError


def multiplication(a, b):
    return int(a) * int(b)


def square(a):
    return float(a) ** 2


def squareroot(a):
    return math.sqrt(float(a))


class Calc:
    result = 0

    def __init__(self):
        pass

    def add(self, a, b):
        self.result = addition(a, b)
        return self.result

    def subtract(self, a, b):
        self.result = subtraction(a, b)
        return self.result

    def div(self, a, b):
        self.result = division(a, b)
        return self.result

    def mult(self, a, b):
        self.result = multiplication(a, b)
        return self.result

    def square(self, a):
        self.result = square(a)
        return self.result

    def sqr_root(self, a):
        self.result = squareroot(a)
        return self.result
