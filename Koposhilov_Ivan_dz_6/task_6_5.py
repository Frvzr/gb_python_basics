import sys

files = sys.argv


def prepare_dataset(files):
    """
    Считывает данные из файлов и возвращает словарь, где:
        ключ — ФИО, значение — данные о хобби (список строковых переменных)
    :param path_users_file: путь до файла, содержащий ФИО пользователей, разделенных запятой по строке
    :param path_hobby_file: путь до файла, содержащий хобби, разделенные запятой по строке
    :return: Dict(str: Union[List[str]|None])
    """

    with open(files[3], 'w+', encoding='utf-8') as f:
        with open(files[1], 'r', encoding='utf-8') as uf, open(files[2], 'r', encoding='utf-8') as hf:
            for line in uf:
                for line_h in hf:
                    f.write(f'{line.rstrip()}: {line_h}')
            f.write(f'\n{line.rstrip()}: {None}')


if __name__ == '__main__':
    if len(files) == 4:
        prepare_dataset(files)
    else:
        print('Введите корректные данные')