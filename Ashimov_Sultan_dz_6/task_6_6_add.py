def main(data):
    with open("bakery.csv", "a", encoding="utf-8") as f:
        f.write(f'{"".join(data)}\n')


if __name__ == '__main__':
    import sys
    data = sys.argv[1:]
    exit(main(data))
