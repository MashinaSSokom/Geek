def num_translate_adv(number):
    translate_dict = {'один': 'one', 'два': 'two', 'три': 'three', 'четыре': 'four', 'пять': 'five', 'шесть': 'six',
                      'семь': 'seven', 'восемь': 'eight', 'девять': 'nine', 'десять': 'ten'}
    if number.istitle() and number.lower() in translate_dict:
        return translate_dict.get(number.lower()).capitalize()
    elif not(number.istitle()) and number in translate_dict:
        return translate_dict.get(number).capitalize()
    else:
        return None


number = input('Введите числительное: ')
print(num_translate_adv(number))