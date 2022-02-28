from functools import wraps


def type_logger(func):
    """Декоратор"""
    @wraps(func)
    def t_logger(*args):
        """Обёртка"""
        print(f'{func.__name__}({args}: {type(args)})')
        logger = func(*args)
        for i in logger:
            print(f'{func.__name__}({i}: {type(i)})')
        return logger

    return t_logger


@type_logger
def calc_cube(x, y):
    """Возведение числа в третью степень"""
    return x ** 3, y ** 3


if __name__ == '__main__':
    a = calc_cube
    print(a(5, 7))
    #print(calc_cube.__name__)
    #print(calc_cube.__doc__)
