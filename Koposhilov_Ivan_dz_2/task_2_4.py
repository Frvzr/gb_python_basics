# На вход будет подаваться список, содержащий искажённые данные с должностями и именами сотрудников:
# Известно, что имя сотрудника всегда в конце строки!
# Обработать все элементы списка и вернуть в качестве результата список, состоящий из фраз вида:
# Подумать, как получить имена сотрудников из элементов списка, как привести их к корректному виду.


def convert_name_extract(list_in: list) -> list:
    """Извлекает имена из элементов и формирует список приветствий."""
    list_out = []
    for item in list_in:
        join_item = ''.join(item)
        split_item = join_item.split()
        list_out.append(f'Привет, {split_item[-1].capitalize()}!')
        
    return list_out


my_list = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй', 'директор аэлита']
result = convert_name_extract(my_list)
print(result)