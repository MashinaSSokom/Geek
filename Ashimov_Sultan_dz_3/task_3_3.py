def thesaurus(*args) -> dict:
    names_dict = {}
    for name in args:  # Чтобы выводился отсортированный словарь, можно изменить args -> sorted(args) - 1 вариант
        if name[0] in names_dict:
            names_dict[name[0]].append(name)
        else:
            names_dict.setdefault(name[0], [name])
    return names_dict


print(thesaurus("Иван", "Мария", "Петр", "Илья"))

# 2 вариант отсортировать уже после получения словаря имен, использую еще один словарь:
# d = {}
# for name_letter in sorted(names_dict):
#     d[name_letter] = names_dict[name_letter]
# print(d)
