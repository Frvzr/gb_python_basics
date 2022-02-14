import os


def create_dir(folders):
    for i in range(1, len(folders)):
        dir_path = os.path.join(folders[0], folders[i])
        if not os.path.exists(dir_path):
            os.makedirs(dir_path)


folders = ['my_project', 'settings', 'mainapp', 'adminapp', 'authapp']
create_dir(folders)
