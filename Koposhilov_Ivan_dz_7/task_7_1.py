import os


def create_dir(folders):
    if not os.path.exists(folders[0]):
        os.mkdir(folders[0])
    
    for i in range(1, len(folders)):
        dir_path = os.path.join(folders[0], folders[i])
        if not os.path.exists(dir_path):
            os.makedirs(dir_path)


folders = ['my_projects', 'settings', 'mainapp', 'adminapp', 'authapp']
create_dir(folders)
