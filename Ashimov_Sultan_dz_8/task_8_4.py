def val_checker(validator):
    def func_taker(func):
        def checker(*args,**kwargs):
            if validator(*args):
                print('Все ок!')
                return func(*args,**kwargs)
            else:
                raise ValueError('Вы ввели неправильный тип данных')
        return checker
    return func_taker




@val_checker(lambda x: x>0)
def print_str(num):
    return f'Вы ввели строку: {num}'

printing = print_str(-6)
print(printing)

# >>> a = calc_cube(5)
# 125
# >>> a = calc_cube(-5)
# Traceback (most recent call last):
#   ...
#     raise ValueError(msg)
# ValueError: wrong val -5