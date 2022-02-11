import yaml
import os


with open('config.yaml') as f:
    templates = yaml.safe_load(f)

for element in templates:
    for k, v in element.items():
        for x in v:
            print(x)


        # dir_path = os.path.join(k, v)
        # print(dir_path)
        # if not os.path.exists(dir_path):
        #     os.makedirs(dir_path)

    