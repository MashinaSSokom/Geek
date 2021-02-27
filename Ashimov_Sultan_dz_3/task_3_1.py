def num_translate(number):
    translate_dict = {'один': 'one', 'два': 'two', 'три': 'three', 'четыре': 'four', 'пять': 'five', 'шесть': 'six',
                      'семь': 'seven', 'восемь': 'eight', 'девять': 'nine', 'десять': 'ten'}
    if number in translate_dict:
        return translate_dict.get(number)
    else:
        return None


number = input('Введите числительное: ')
print(num_translate(number))
