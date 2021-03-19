def main(start = None, data = None):
    with open("bakery.csv", "r+", encoding="utf-8") as f:
        text = f.readlines()
        if len(text) < int(start):
            return print('Вы ввели еккоректный номер строки')
        text[int(start)-1] = f'{data}\n'
    with open("bakery.csv", "w", encoding="utf-8") as f:
        f.writelines(text)


if __name__ == '__main__':
    import sys
    start, data = sys.argv[1:]
    exit(main(start, data))
