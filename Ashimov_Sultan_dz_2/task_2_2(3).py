raw = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
for idx in range(len(raw)):
    if raw[idx].isdecimal():
        raw[idx] = f'"{raw[idx]:0>2}"'
    elif raw[idx][0] == '+' or raw[idx][0] == '-':
        raw[idx] = f'"{raw[idx][0]}{raw[idx][1:]:0>2}"'
print('Полученный список:', raw)
print('Строка из полученного списка:', " ".join(raw))