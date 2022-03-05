#обрабатывает ошибку деления на 0
class CustomZeroDivisionError(Exception):

    def __init__(self, number_1, number_2):
        self.number_1 = number_1
        self.number_2 = number_2

    @staticmethod
    def devide(number_1, number_2):
        try:
            return number_1 / number_2
        except:
            return 'на ноль делить нельзя'

e = CustomZeroDivisionError(10, 2)
print(e.devide(2, 0))
print(CustomZeroDivisionError.devide(2, 2))

try:
    print(e.devide(10, 0))
except ValueError as err:
    print(err)  
