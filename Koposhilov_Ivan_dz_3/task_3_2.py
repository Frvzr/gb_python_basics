#*(вместо задачи 1) Перепишите функцию из задания 1 изменив название на num_translate_adv(): 
# реализовать корректную работу с числительными, начинающимися с заглавной буквы — результат тоже должен быть с заглавной.


def num_translate_adv(key: str) -> str:
    """переводит числительное с английского на русский """

    numbers = {
        'zero': ['ноль', 'Ноль'],
        'one': ['один', 'Один'],
        'two': ['два', 'Два'],
        'three': ['три','Три'],
        'four': ['четыре', 'Четыре'],
        'five': ['пять', 'Пять'],
        'six': ['шесть', 'Шесть'],
        'seven': ['семь', 'Семь'],
        'eight': ['восемь', 'Восемь'],
        'nine': ['девять', 'Девять'],
        'ten': ['десять', 'Десять']
    }

    new_key = key.lower()
    if new_key in numbers:
        if key.istitle():
            return numbers[new_key][1]
        elif key.islower():
            return numbers[new_key][0]
    else:
        return None


print(num_translate_adv("One"))
print(num_translate_adv("two"))
print(num_translate_adv("oNe"))
print(num_translate_adv("ONe"))
print(num_translate_adv("Один"))
print(num_translate_adv("1"))
print(num_translate_adv("eleven"))