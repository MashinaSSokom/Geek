def thesaurus_adv(*args):
    names_dict = {}
    all_full_names = list(*args)
    for full_name in all_full_names:
        name, last_name = full_name.split()
        if last_name[0] in names_dict:  # Проверяем нахождение в словаре первой буквы фамилии
            if name[0] in names_dict[last_name[0]]:  # Проверяем нахождение в словаре первой буквы имени
                names_dict[last_name[0]][name[0]].append(full_name)
            else:
                names_dict[last_name[0]].setdefault(name[0], full_name)
        else:
            names_dict.setdefault(last_name[0], {name[0]:[full_name]})
    return names_dict


print(thesaurus_adv("Иван Сергеев", "Инна Серова", "Петр Алексеев", "Илья Иванов", "Анна Савельева"))
