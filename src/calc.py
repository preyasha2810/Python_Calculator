def addition(a, b):
    return a + b

class Calc:
    result = 0

    def  __init__(self):

        x = 2 + 3
        self.result = x

    def add(self, a, b):
        self.result = a + b
        return addition(a, b)