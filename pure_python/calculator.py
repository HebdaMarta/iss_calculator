class Calculator:
    def __init__(self, op1: float, op2: float):
       self.__op1 = op1
       self.__op2 = op2

    @property
    def op1(self):
        return self.__op1

    @property
    def op2(self):
        return self.__op2

    @op1.setter
    def op1(self, value: float):
        self.__op1 = value

    @op2.setter
    def op2(self, value: float):
        self.__op2 = value

    def sum(self):
        return self.__op1 + self.__op2

    def subtract(self):
        return self.__op1 - self.__op2

    def multiply(self):
        return self.__op1 * self.__op2

    def divide(self):
        if self.__op2 == 0:
            raise ZeroDivisionError("Cannot divide by zero")
        return self.__op1 / self.__op2

    def __repr__(self):
        return f"Calculator(op1={self.__op1}, op2={self.__op2})"



