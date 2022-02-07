

def prepare_dataset(path_users_file: str, path_hobby_file: str):
    """
    Считывает данные из файлов и возвращает словарь, где:
        ключ — ФИО, значение — данные о хобби (список строковых переменных)
    :param path_users_file: путь до файла, содержащий ФИО пользователей, разделенных запятой по строке
    :param path_hobby_file: путь до файла, содержащий хобби, разделенные запятой по строке
    :return: Dict(str: Union[List[str]|None])
    """
    with open('users_hobby.txt', 'w+', encoding='utf-8') as f:
        with open(path_users_file, 'r', encoding='utf-8') as uf, open(path_hobby_file, 'r', encoding='utf-8') as hf:
            for line in uf:
                for line_h in hf:
                    f.write(f'{line.rstrip()}: {line_h}')
            f.write(f'\n{line.rstrip()}: {None}')


prepare_dataset('users.csv', 'hobby.csv')
