# Реализовать склонение слова процент во фразе N процентов. 
# Вывести эту фразу на экран отдельной строкой для каждого из чисел в интервале от 1 до 100:

def transform_string(number: int) -> str:
    if number != 11 and number % 10 == 1:
        return f'{number} процент'
    elif (number % 10 == 2 or number % 10 == 3 or number % 10 == 4) and number != 12 and number != 13 and number != 14:
        return f'{number} процента'
    else:
        return f'{number} процентов'

for n in range(1, 101):
    print(transform_string(n))

    #test change for pull request