# Написать функцию num_translate(), переводящую числительные от 0 до 10 c английского на русский язык.
# Если перевод сделать невозможно, вернуть None.


def num_translate(key: str) -> str:
    """переводит числительное с английского на русский """
    numbers = {
        'zero': 'ноль',
        'one': 'один',
        'two': 'два',
        'three': 'три',
        'four': 'четыре',
        'five': 'пять',
        'six': 'шесть',
        'seven': 'семь',
        'eight': 'восемь',
        'nine': 'девять',
        'ten': 'десять'
    }
    # str_out = numbers.get(value)
    # return str_out
    if key in numbers:
        str_out = numbers[key]
    else:
        str_out = None
    return str_out

numbers_eng = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'eleven']

for i in numbers_eng:
    print(num_translate(i))
