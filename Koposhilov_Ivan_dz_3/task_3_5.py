"""
Реализовать функцию get_jokes(), возвращающую n шуток,
сформированных из трех случайных слов, взятых из трёх списков (по одному из каждого):
"""

import random

nouns = ["автомобиль", "лес", "огонь", "город", "дом", "огород"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью", "в субботу"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий", "суровый"]

"""
1-ое решение с повторяющимися значениями из глобальной области
"""

def get_jokes(count: int) -> list:
    """
    Возвращает список шуток в количестве count
    """

    list_out = []

    for _ in range(count):
        list_out.append(f'{random.choice(nouns)} {random.choice(adverbs)} {random.choice(adjectives)}')
    
    return list_out


print(get_jokes(2))
print(get_jokes(10))

"""
2-ое решение: если значение count больше длины самого короткого списка
сначала достает рандомно/повторяющиеся, когда оставшееся кол-во доходит до длины списка, 
извлекает неповторяющиеся элементы, если длина меньше списка, достает уникальные значения
"""
def get_jokes_adv(count: int) -> list:
    """
    Возвращает список шуток в количестве count
    """

    nouns_local = ["автомобиль", "лес", "огонь", "город", "дом", "огород"]
    adverbs_local = ["сегодня", "вчера", "завтра", "позавчера", "ночью", "в субботу"]
    adjectives_local = ["веселый", "яркий", "зеленый", "утопичный", "мягкий", "суровый"]

    list_out = []

    length = min([len(nouns_local), len(adverbs_local), len(adjectives_local)])

    for _ in range(count):
        if count <= length:
            noun = nouns_local.pop(random.randrange(len(nouns_local)))
            adverb = adverbs_local.pop(random.randrange(len(adverbs_local)))
            adjective = adjectives_local.pop(random.randrange(len(adjectives_local)))
            list_out.append(f'{noun} {adverb} {adjective}')
        else:
            list_out.append(f'{random.choice(nouns)} {random.choice(adverbs)} {random.choice(adjectives)}')
            count -= 1

    return list_out


print(get_jokes_adv(5))
print(get_jokes_adv(10))


"""
3-ое решение: с flag, разрешающий или запрещающий повторы слов в шутках 
(когда каждое слово можно использовать только в одной шутке)
"""
def get_jokes_adv_flag(count: int, flag) -> list:
    """Возвращает список шуток в количестве count"""

    nouns_local = ["автомобиль", "лес", "огонь", "город", "дом", "огород"]
    adverbs_local = ["сегодня", "вчера", "завтра", "позавчера", "ночью", "в субботу"]
    adjectives_local = ["веселый", "яркий", "зеленый", "утопичный", "мягкий", "суровый"]
    
    list_out = []

    # находим минимальное значение, т.к уникальных связок может быть не более чем длина списка
    length = min([len(nouns_local), len(adverbs_local), len(adjectives_local), count])

    if flag:
        for _ in range(length):
            noun = nouns_local.pop(random.randrange(len(nouns_local)))
            adverb = adverbs_local.pop(random.randrange(len(adverbs_local)))
            adjective = adjectives_local.pop(random.randrange(len(adjectives_local)))
            list_out.append(f'{noun} {adverb} {adjective}')
    else:
        for _ in range(count):
            list_out.append(f'{random.choice(nouns)} {random.choice(adverbs)} {random.choice(adjectives)}')

    return list_out

flag = False
print(get_jokes_adv_flag(5, flag))
print(get_jokes_adv_flag(10, flag))
