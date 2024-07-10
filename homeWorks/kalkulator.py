class calculator:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def add(self):
        return self.num1 + self.num2

    def sub(self):
        return self.num1 - self.num2

    def mul(self):
        return self.num1 * self.num2

    def truediv(self):
        if self.num2 != 0:
            return self.num1 / self.num2
        else:
            return "cannot divide by zero"

calc = calculator(10, 5)

# Test the methods
print("addition:", calc.add())
print("subtraction:", calc.sub())
print("multiplication:", calc.mul())
print("division:", calc.truediv())