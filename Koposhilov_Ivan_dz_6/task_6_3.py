import json


def prepare_dataset(path_users_file: str, path_hobby_file: str) -> dict:
    """
    Считывает данные из файлов и возвращает словарь, где:
        ключ — ФИО, значение — данные о хобби (список строковых переменных)
    :param path_users_file: путь до файла, содержащий ФИО пользователей, разделенных запятой по строке
    :param path_hobby_file: путь до файла, содержащий хобби, разделенные запятой по строке
    :return: Dict(str: Union[List[str]|None])
    """
    users_hobby = {}

    with open(path_users_file, 'r', encoding='utf-8') as uf:
        users = uf.readlines()
        users = [line.rstrip() for line in users]

    with open(path_hobby_file, 'r', encoding='utf-8') as hf:
        hobby = hf.readlines()
        hobby = [line.rstrip() for line in hobby]
    
    users_hobby = dict(zip(users, hobby))
    temp = {users_hobby.setdefault(key) for key in users}

    if len(users) < len(hobby):
        return 1
    else:
        return users_hobby # верните словарь, либо завершите исполнение программы кодом 1


dict_out = prepare_dataset('users.csv', 'hobby.csv')
with open('task_6_3_result.json', 'w', encoding='utf-8') as fw:
    json.dump(dict_out, fw, ensure_ascii=False, indent=2)