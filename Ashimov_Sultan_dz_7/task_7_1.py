import os
def create_start_tree(main_dir = 'my_project', dirs_to_create = ['settings', 'mainapp', 'adminapp', 'authapp']):
    if not os.path.exists(main_dir):
        os.mkdir(main_dir)
        for directory in dirs_to_create:
            os.makedirs(fr'{main_dir}\{directory}')
    else:
        for directory in dirs_to_create:
            if not os.path.exists(os.path.join(main_dir, directory)):
                os.makedirs(fr'{main_dir}\{directory}')

create_start_tree()