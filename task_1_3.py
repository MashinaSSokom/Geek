# По идее должно сработать с любым числом

number = int(input("Введите число: "))
if 10 < number%100 < 20:
    print(number, 'процентов')
elif number % 10 == 1:
    print(number, 'процент')
elif number % 10 in [2, 3, 4]:
    print(number, 'процента')
else:
    print(number, 'процентов')
