import itertools
import sys

tutors = ['Иван', 'Анастасия', 'Петр', 'Сергей', 'Дмитрий', 'Борис', 'Елена', 'Эдгар', 'Борис']
classes = ['9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А']
gen = itertools.zip_longest(tutors, classes, fillvalue=None)
print(type(gen), sys.getsizeof(gen))
print(*gen, sep='\n')
