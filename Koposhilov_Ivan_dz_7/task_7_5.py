import os
from os.path import relpath
from sys import path
import json


def found_files(files_size, result):
    # folder_files = set()
    # folder = os.getcwd()
    # for root, dirs, files in os.walk(folder):
    #     for item in files:
    #         ext = item.rsplit('.')[-1].lower()
    #         rel_path = relpath(os.path.join(root, item), folder)
    #         folder_files.add(ext)
    #         print(folder_files)
    #         path_file = os.path.join(root, item)
    #         size_file = os.path.getsize(path_file)
    #         group_size = min(filter(lambda x: size_file < x, files_size))
    #         result[group_size] += 1

    # # for ext, files in sorted(folder_files.items(), key=lambda x: len(x[1]), reverse=True):
    # #     print(ext)
    # return result
    value_list = [100, 0, [], 1000, 0, [], 10000, 0, [], 100000, 0, []]
    folder = os.path.dirname(os.path.abspath(__file__))
    for item in os.scandir(folder):
        if os.path.isfile(item):
            ext = item.name.rsplit('.', maxsplit=1)[-1].lower()
            path_file = os.path.join(folder, item)
            size_file = os.path.getsize(path_file)
            group_size = min(filter(lambda x: size_file < x, files_size))
            idx = value_list.index(group_size)
            value_list[idx + 1] += 1
            if ext not in value_list[idx + 2]:
                value_list[idx + 2].append(ext)
            counter = 1
            for key in result:
                result[key] = (value_list[counter], value_list[counter + 1])
                counter += 3

    return result
            

files_size = [100, 1000, 10000, 100000]
result = dict.fromkeys(files_size, 0)

print(found_files(files_size, result))

with open('summary.json', 'w+', encoding='utf-8') as f:
    json.dump(result, f, indent=6)