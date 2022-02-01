def get_uniq_numbers(src: list):
    """
    Генератор, выводящий элементы списка не имеющих повторений
    :src: list с значениями
    :return: 
    """
    # первый вариант
    # result = []
    # for num in src:
    #     if src.count(num) == 1:
    #         result.append(num)
    # return result

    # второй вариант
    # result = [num for num in src if src.count(num) == 1]
    # return result

    # третий вариант
    unique_numbers = set()
    tmp = set()
    for num in src:
        if num not in tmp:
            unique_numbers.add(num)
        else:
            unique_numbers.discard(num)
        tmp.add(num)
    result = [num for num in src if num in unique_numbers]
    return result


src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
print(*get_uniq_numbers(src))
