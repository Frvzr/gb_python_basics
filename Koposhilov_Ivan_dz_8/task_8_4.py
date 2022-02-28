from functools import wraps

user_validation = ['Ivan', 'Petr', 'Oksana']


def val_checker(callback):
    """Декоратор с аргументами"""
    def get_check(func):
        """Основной декаратор"""
        @wraps(func)
        def checker(*args):
            """Обёртка"""
            for i in args:
                if callback not in user_validation:
                    msg = f'wrong val {i}'
                    raise ValueError(msg)
                else:
                    _check = func(*args)
                    return _check
                    
        return checker

    return get_check


@val_checker('Petr')
def calc_cube(x):
    """Возведение числа в третью степень"""
    return x ** 3


@val_checker('Oleg')
def calc_cube_2(x):
    """Возведение числа в третью степень"""
    return x ** 3


if __name__ == '__main__':
    print(calc_cube(3))
    #print(calc_cube_2(-3))
    print(calc_cube_2('ss'))
