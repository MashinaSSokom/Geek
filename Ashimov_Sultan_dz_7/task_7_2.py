import os
import yaml


def depth_maker(data, path = ''):
    for folder, el in data.items():
        folder_path = os.path.join(path, folder)
        os.makedirs(folder_path, exist_ok=True)
        if isinstance(el, dict):
            depth_maker(el, folder_path)
        else:
            for item in el:
                if isinstance(item, dict):
                    depth_maker(item, folder_path)
                elif isinstance(item, str):
                    item_path = os.path.join(folder_path, item)
                    f = open(item_path, 'w')
                    f.close()


with open("config.yaml", encoding="utf-8") as f:
    config = yaml.safe_load(f)
    depth_maker(config)
