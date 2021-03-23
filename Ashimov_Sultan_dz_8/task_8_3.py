def decorator_function(func):
    def inside_decorator(*args, **kwargs):
        for arg in args:
            print(f'Аргумент: {args} имеет тип: {type(arg)}')
        return func(*args, **kwargs)

    return inside_decorator


@decorator_function
def func(*args):
    return f'Принял на вход:\n' \
           f'{args}'


print(func(1, 'str', [1, 'str']))
