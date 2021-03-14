def main(start = None, finish = None):
    if start is None and finish is None:
        with open("bakery.csv",encoding="utf-8") as f:
            for line in f:
                print(line, end='')
    elif finish is None:
        with open("bakery.csv", encoding="utf-8") as f:
            for _ in range(int(start)-1):
                f.readline()
            for line in f:
                print(line, end='')
    else:
        with open("bakery.csv", encoding="utf-8") as f:
            for _ in range(int(start)-1):
                f.readline()
            for rep in range(int(finish)-int(start)+1):
                print(f.readline(), end='')


if __name__ == '__main__':
    import sys
    if len(sys.argv[1:]) == 1:
        start = sys.argv[1]
        exit(main(start))
    elif len(sys.argv[1:]) == 2:
        start, finish = sys.argv[1:]
        exit(main(start, finish))
    else:
        exit(main())
