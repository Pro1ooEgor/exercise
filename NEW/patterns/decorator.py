# the first method of implementing the decorator
def test_decorator(func):
    def wrapper():
        print('  /\  ')
        func()
        print('/    \ ')

    return wrapper


def test_func():
    print(' /  \ ')


test_func = test_decorator(test_func)
test_func()


# the second method of implementing the decorator
def test_decorator(func):
    def wrapper():
        print('  /\  ')
        func()
        print('/    \ ')

    return wrapper


@test_decorator
def test_func():
    print(' /  \ ')


test_func()


# decorator with arguments passed to the function
def decorator_with_arguments(func):
    def wrapper(*args):
        for i in args:
            print('Полученный параметр: ' + i)
        func()

    return wrapper


@decorator_with_arguments
def test_func(*args):
    print('Hello world')


test_func('Misha', 'Egor', 'Artem')


def test_decorator(age):
    def decorator(func):
        def wrapper(name):
            print('Name: ' + name + ', age: ' + str(age))
            return func(name)
        return wrapper
    return decorator


@test_decorator(13)
def test_func(name):
    print('Name in function: ' + name)


test_func('Egor')
