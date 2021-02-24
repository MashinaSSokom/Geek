def number_sum(number, digit_sum=0):  # Находит сумму цифр в числе
    for idx in range(len(str(number))):
        digit_sum += number%10
        number = number // 10
    return digit_sum

qubes = [int(i)**3 for i in range(1, 1000,2)]
print('Длина', len(qubes))
total_1 = 0  # Сумма в пункте a)
total_2 = 0  # Сумма в пункте b)
for number in qubes:
    if number_sum(number) % 7 == 0:  # находим сумму для пунка a
        total_1 += number
    if number_sum(number+17) % 7 == 0:  # находим сумму для пункта b,c (сразу посчитал сумму без созданния доп. списка)
        total_2 += (number+17)

print('Первая сумма', total_1)
print('Вторая сумма', total_2)
