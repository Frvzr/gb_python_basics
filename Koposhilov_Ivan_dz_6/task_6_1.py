from pprint import pprint


def get_parse_attrs(line: str) -> tuple:
    """
    Парсит строку на атрибуты и возвращает кортеж атрибутов (<remote_addr>, <request_type>, <requested_resource>)
    """
    line_list = line.split()
    return line_list[0], line_list[5], line_list[6]    # верните кортеж значений <remote_addr>, <request_type>, <requested_resource>
    

list_out = list()
with open('nginx_logs.txt', 'r', encoding='utf-8') as fr:
    for line in fr:
        list_out.append(get_parse_attrs(line))


pprint(list_out)