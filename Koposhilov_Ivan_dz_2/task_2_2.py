# a) Необходимо его обработать — обособить каждое целое число (вещественные не трогаем) кавычками (добавить кавычку до и кавычку после элемента списка, являющегося числом) и дополнить нулём до двух целочисленных разрядов:
# b) Сформировать из обработанного списка строку:
# *(вместо задачи 2) Решить задачу 2, не создавая новый список (как говорят, in place). Эта задача намного серьёзнее, чем может сначала показаться.

def convert_list_in_str(list_in: list) -> str:
    #print(id(list_in))
    i = 0
    while i < len(list_in):
        if list_in[i].isdigit():
            list_in.insert(i, '"')
            list_in[i+1] = f'{int(list_in[i+1]):02d}'
            list_in.insert(i + 2, '"')
            i += 2
        elif not list_in[i].isalpha():
            list_in.insert(i, '"')
            list_in[i+1] = f'{int(list_in[i+1]):+03d}'
            list_in.insert(i + 2, '"')
            i += 2
        elif not list_in[i].isalpha():
            list_in.insert(i, '"')
            list_in[i+1] = f'{int(list_in[i+1]):-03d}'
            list_in.insert(i + 2, '"')
            i += 2
        i += 1
    # сравниваем id до и после
    #print(id(list_in)) 
    #print(list_in)

    # Преобразовываем список в строку
    str_out = ' '.join(list_in)
    count_simbol = str_out.count('"')
    count = 0

    # избавляемся от пробелов между " и символом
    for i in range(len(str_out) - count_simbol):
        if str_out[i] == '"':
            count += 1
            # если count нечетное, то это открывающая "
            if count % 2 != 0:
                # за счет срез избавляемся от пробела после "
                str_out = str_out[:i + 1] + str_out[i+2:]
            # если count четное, то это закрывающаяся "
            else:
                # за счет срез избавляемся от пробела перед "
                str_out = str_out[:i-1] + str_out[i:]              

    return str_out


my_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '-5', 'градусов']
result = convert_list_in_str(my_list)
print(result)