import sys

command = sys.argv

if len(command) != 2:
    print('Введите корректные данные')
else:
    with open('backery.csv', 'a', encoding='utf-8') as f:
        print(command[1], file=f)
