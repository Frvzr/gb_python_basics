from functools import wraps


def val_checker(check=0):
    def get_check(func):
        @wraps(func)
        def checker(*args):
            """Обёртка"""
            for i in args:
                if not str(i).isdigit() or i < 0:
                    msg = f'wrong val {i}'
                    raise ValueError(msg)
                else:
                    _check = func(*args)
                    return _check

        return checker

    return get_check


@val_checker(check=1)
def calc_cube(x):
    """Возведение числа в третью степень"""
    return x ** 3


if __name__ == '__main__':
    a = calc_cube
    print(a(7))
    print(calc_cube('ss'))
