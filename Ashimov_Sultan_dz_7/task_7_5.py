import os

def get_sizes(folder_path):
    sizes = {}
    for item in os.listdir(folder_path):
        if '.' in item:
            size = 0
            file_size = os.stat(os.path.join(folder_path, item)).st_size
            file_extension = os.path.join(folder_path, item).split('.')[-1]
            while file_size > 0:
                size += 1
                file_size //= 10
            if 10 ** size not in sizes and size != 0:
                sizes[10 ** size] = (1, [file_extension])
            elif size == 0:
                sizes[size] = (1, [file_extension])
            else:
                names = sizes[10 ** size][1]
                if file_extension not in names:
                    names.append(file_extension)
                sizes[10 ** size] = (sizes[10 ** size][0] + 1, names)
        else:
            continue
    return sizes


folder_path = os.getcwd()
print(get_sizes(folder_path))
