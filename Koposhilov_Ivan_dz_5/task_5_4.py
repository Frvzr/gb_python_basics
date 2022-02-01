from time import perf_counter
import sys

def get_numbers(src: list):
    """
    Генератор, выводящий значения из списка, которые больше предыдущего значения
    :src: list с значениями
    :return: generator
    """
    # первый вариант
    # start = perf_counter()
    # result = []
    # for i in range(0, len(src) - 1):
    #     if src[i] < src[i + 1]:
    #         result.append(src[i + 1])
    # print(sys.getsizeof(result), perf_counter() - start) #120 0.0000165
    # return result

    #второй вариант
    #start = perf_counter()
    result = (src[i + 1] for i in range(0, len(src) - 1) if src[i] < src[i + 1])
    #print(sys.getsizeof(result), perf_counter() - start) #112 0.0000075
    return result


src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
print(*get_numbers(src))