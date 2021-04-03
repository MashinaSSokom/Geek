class ZeroException(Exception):
    def __init__(self, txt):
        self.txt = txt


try:
    p1 = int(input('Введите первое число: '))
    p2 = int(input('Введите второе число число: '))
    if p2 == 0:
        raise ZeroException('Деление на ноль!')
except ZeroException as err:
    print(err)
else:
    print(p1 / p2)