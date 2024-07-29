class Riyazi:
    @staticmethod
    def __check_value(num1, num2):
        try:
            if isinstance(num1, (int, float)) and isinstance(num2, (int, float)):
                return num1, num2
            elif isinstance(num1, (int, float)) and not isinstance(num2, (int, float)):
                raise ValueError("Second argument must be an int or float.")
            elif not isinstance(num1, (int, float)) and isinstance(num2, (int, float)):
                raise ValueError("First argument must be an int or float.")
            elif not isinstance(num1, (int, float)) and not isinstance(num2, (int, float)):
                raise ValueError("Both arguments must be int or float.")
        except ValueError as e:
            raise e

    @staticmethod
    def Add(num1, num2):
        try:
            a, b = Riyazi.__check_value(num1, num2)
            return a + b
        except ValueError as e:
            raise e
    def Subtract(num1, num2):
        try:
            a, b = Riyazi.__check_value(num1, num2)
            return a - b
        except ValueError as e:
            raise e
    def Multiplication(num1, num2):
        try:
            a, b = Riyazi.__check_value(num1, num2)
            return a * b
        except ValueError as e:
            raise e
    def __check_zero(num2):
        if num2 != 0:
            return num2
        else:
            raise ValueError("Do not insert 0")

    def Division(num1, num2):
        try:
            a, b = Riyazi.__check_value(num1, num2)
            b = Riyazi.__check_zero(num2)
            return a / b
        except ValueError as e:
            raise e
