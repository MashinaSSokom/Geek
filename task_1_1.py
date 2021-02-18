def time_translate(duration):  # Трансформирует время в нужный формат
    s = duration % 60
    m = ((duration - s) // 60) % 60
    h = (duration // 60 ** 2) % 24
    d = duration // (60 ** 2 * 24)
    return s, m, h, d


durations = [int(i) for i in input().split()]
for duration in durations:
    s, m, h, d = time_translate(duration)
    print('duration =', duration)
    if m == 0 and h == 0 and d == 0:
        print(s, 'сек')
    elif h == 0 and d == 0:
        print(m, 'мин', s, 'сек')
    elif d == 0:
        print(h, 'час', m, 'мин', s, 'сек')
    else:
        print(d, 'дн', h, 'час', m, 'мин', s, 'сек')
