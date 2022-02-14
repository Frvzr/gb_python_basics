import sys

command = sys.argv

if len(command) != 3:
    print('Введите корректные данные: номер записи - новое значение')
else:
    with open('backery.csv', 'r+', encoding='utf-8') as f:
        for i, line in enumerate(f, 1):
            if i == int(command[1]):
                line = line.replace(line, command[2])
                break

    # with open('backery.csv', 'r+', encoding='utf-8') as f:
