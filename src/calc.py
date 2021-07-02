import math


def addition(a, b):
    return a + b

def subtraction(a, b):
    return a - b

def division(a, b):
    return a / b

def multiplication(a, b):
    return a * b

def square(a):
    return a**2

def squareroot(a):
    return math.sqrt(a)

class Calc:
    result = 0

    def  __init__(self):
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

    def square_root(self, a):
        self.result = squareroot(a)
        return self.result
