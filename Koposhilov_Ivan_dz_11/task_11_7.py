class ComplexNumber:

    def __init__(self, real, imaginary):
        """
        Определяем части комплексного числа
        real: действительная часть
        imaginary: мнимая часть 
        """
        self.real = real
        self.imaginary = imaginary

    def __add__(self, other):
        """
        Функция для сложения между двумя комплексными числами
        """
        return ComplexNumber(self.real + other.real, self.imaginary + other.imaginary)

    def __mul__(self, other):
        """
        Функция для умножения между двумя комплексными числами
        """
        return ComplexNumber(self.real * other.real, self.imaginary * other.imaginary)
    
    def __str__(self):
        """
        Функция для создания комплексного числа
        """
        return f'{self.real}{self.imaginary}j' if self.imaginary < 0 else f'{self.real}+{self.imaginary}j'
        
        # if self.imaginary < 0:
        #     return f'{self.real}{self.imaginary}j' 
        # else:
        #     return f'{self.real}+{self.imaginary}j'


com_num_1 = ComplexNumber(1, -3)
com_num_2 = ComplexNumber(1, 2)
print(type(com_num_1), com_num_1)
print(type(com_num_2), com_num_2)
print(type(com_num_1 + com_num_2), com_num_1 + com_num_2)
print(type(com_num_1 * com_num_2), com_num_1 * com_num_2)