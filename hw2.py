class Calculator():
    def __init__(self,a,b) -> None:
        self.a = a
        self.b = b
    def __add__(self):
        return self.a+self.b
    def __sub__(self):
        return self.a-self.b
    def __mul__(self):
        return self.a*self.b
    def __div__(self):
        return self.a/self.b
calc = Calculator(10,5)
print(calc.__add__())
print(calc.__sub__())
print(calc.__mul__())
print(calc.__div__())