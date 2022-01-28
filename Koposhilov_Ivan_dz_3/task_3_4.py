"""
Написать функцию thesaurus_adv(), принимающую в качестве аргументов строки в формате «Имя Фамилия» и
возвращающую словарь, в котором ключи — первые буквы фамилий, а значения — словари, реализованные по схеме предыдущего
задания и содержащие записи, в которых фамилия начинается с соответствующей буквы.
"""


def thesaurus_adv(*args) -> dict:
    # корректно работает при правильном внесении данных Имя Фамилия
    dict_out = {} 
    for i in range(len(args)):
        count = 0
        for j in args[i]:
            if j.isupper():
                count += 1
                if count % 2 == 0:
                    if j not in dict_out:
                        dict_out[j] = {args[i][0]: [args[i]]}
                    else:
                        if args[i][0] not in dict_out[j]:
                            dict_out[j].update({args[i][0]: [args[i]]})
                        else:
                            dict_out[j][args[i][0]].append(args[i]) 
    return dict_out


print(thesaurus_adv("Иван Сергеев", "Инна Серова", "Петр Алексеев", "Илья Иванов", "Анна Савельева", "Иван Иванов", "Алексей Петров"))