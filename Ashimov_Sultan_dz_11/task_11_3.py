class IntegerError(Exception):
    def __init__(self, text):
        self.text = text


k = int(input('Введите длину списка: '))
l = []
for idx in range(k):
    try:
        el = input('Введите число для добавления в список: ')
        if not el.isdigit():
            raise IntegerError('Введено не число!')
        l.append(int(el))
    except IntegerError as err:
        print(err)
        exit(1)
print(l)