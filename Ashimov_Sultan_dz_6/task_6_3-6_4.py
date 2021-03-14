with open("users.csv", encoding="utf-8") as f_users, open("hobby.csv", encoding="utf-8") as f_hobbies,\
        open("users_hobby.txt", "w", encoding="utf-8") as f_write:
    result = dict()
    for user in f_users:
        hobby = f_hobbies.readline()
        if hobby != '':
            result[user[:-1]] = hobby[:-1]
            f_write.write(f'{user[:-1]} : {hobby[:-1]}\n')
        else:
            result[user[:-1]] = None
            f_write.write(f'{user[:-1]} : {None}\n')
    print(result)
    if f_hobbies.readline() != '':
        exit(1)
