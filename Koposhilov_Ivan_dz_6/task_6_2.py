import chunk
from pprint import pprint


def get_parse_attrs(line: str) -> tuple:
    """
    Парсит строку на атрибуты и возвращает кортеж атрибутов (<remote_addr>, <count>)
    """
    line_list = line.split()
    return line_list[0]   # верните кортеж значений <remote_addr>, <request_type>, <requested_resource>
    

def search_spammer(list_out):
    count_dict ={}
    for i in list_out:
        if i not in count_dict:
            counter = list_out.count(i)
            count_dict[i] = counter
    max_key = max(count_dict, key=count_dict.get) 
    return max_key, count_dict[max_key]


list_out = list()
with open('nginx_logs.txt', 'r', encoding='utf-8') as fr:
    for line in fr:
        list_out.append(get_parse_attrs(line))

list_out = search_spammer(list_out)


pprint(list_out)