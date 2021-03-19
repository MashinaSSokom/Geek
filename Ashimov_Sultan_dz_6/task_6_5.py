def main(args):
    users_filename = args[0]
    hobby_filename = args[1]
    output_filename = args[2]

    with open(users_filename, encoding="utf-8") as f_users, open(hobby_filename, encoding="utf-8") as f_hobbies,\
            open(output_filename, "w", encoding="utf-8") as f_write:
        for user in f_users:
            hobby = f_hobbies.readline()
            if hobby != '':
                f_write.write(f'{user[:-1]} : {hobby[:-1]}\n')
            else:
                f_write.write(f'{user[:-1]} : {None}\n')
        if f_hobbies.readline() != '':
            exit(1)

if __name__ == '__main__':
    import sys
    exit(main(sys.argv[1:]))