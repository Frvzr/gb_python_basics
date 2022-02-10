import os


def found_files(files_size, result):
    folder = os.getcwd()
    for item in os.scandir(folder):
        if os.path.isfile(item):
            path_file = os.path.join(folder, item)
            size_file = os.path.getsize(path_file)
            group_size = min(filter(lambda x: size_file < x, files_size))
            result[group_size] += 1
    return result
            

files_size = [100, 1000, 10000, 100000, 1000000, 10000000, 100000000, 1000000000, float("inf")]
result = dict.fromkeys(files_size, 0)

print(found_files(files_size, result))