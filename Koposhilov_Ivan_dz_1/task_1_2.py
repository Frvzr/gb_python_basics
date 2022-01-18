# a) Создать список, состоящий из кубов нечётных чисел от 1 до 1000 (куб X - третья степень числа X):
# Вычислить сумму тех чисел из этого списка, сумма цифр которых делится нацело на 7.
# b) К каждому элементу списка добавить 17 и заново вычислить сумму тех чисел из этого списка, сумма цифр которых делится нацело на 7.
# *c) Решить задачу под пунктом b, не создавая новый список. (если будете решать - либо создайте доп. функцию, либо перепишите существующую sum_list_2)

def sum_list_1(dataset: list) -> int:
    total_sum = 0
    for data in dataset:
        sum = 0
        new_data = data
        while new_data !=0:
            sum += new_data % 10
            new_data //= 10
        if sum % 7 == 0:
            total_sum += data
    return total_sum


def sum_list_2(dataset: list) -> int:
    for i in range(len(dataset)):
        dataset[i] += 17
    return sum_list_1(dataset)


numbers = [i**3 for i in range(1000) if i % 2 != 0]
result_1 = sum_list_1(numbers)
print(result_1)
result_2 = sum_list_2(numbers)
print(result_2)

#test change for pull request