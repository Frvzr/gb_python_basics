import os
import shutil

BASE_DIR = 'my_project'

for root, dirs, files in os.walk(BASE_DIR):
    for dir in dirs:
        if dir == 'templates':
            my_path = os.path.join(root, dir)
            new_path = os.path.join(BASE_DIR, 'templates', root)
            if not os.path.exists(new_path):
                shutil.copytree(my_path, new_path)
            for item in files:
                src_file = os.path.join(root, item)
                print(src_file)
       