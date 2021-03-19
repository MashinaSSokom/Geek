import os
import shutil


def grab_templates(path_to_destination, source_path, name='templates'):
    for item in os.listdir(source_path):
        if item == name:
            for el in os.listdir(os.path.join(source_path, item)):
                print('Копирую папку', os.path.join(os.path.join(source_path, item), el))
                print('Копирую сюда', os.path.join(path_to_destination, os.path.join(source_path, item).split('\\')[-2]))
                shutil.move(os.path.join(os.path.join(source_path, item), el),
                            os.path.join(path_to_destination, os.path.join(source_path, item).split('\\')[-2]),
                            copy_function=shutil.copytree)
            print('Удаляю папку', os.path.join(os.path.join(source_path, item)))
            os.rmdir(os.path.join(os.path.join(source_path, item)))
            continue
        elif '.' in item:
            continue
        grab_templates(path_to_destination, os.path.join(source_path, item), name)


name = 'templates'
name_of_source_folder = 'my_project'
source_path = os.path.join(os.getcwd(), name_of_source_folder)
path_to_destination = os.path.join(os.getcwd(), name)
print('Стартовый путь', source_path)
print('Конечный путь:', path_to_destination)
os.makedirs(path_to_destination, exist_ok=True)
grab_templates(path_to_destination, source_path, name)
