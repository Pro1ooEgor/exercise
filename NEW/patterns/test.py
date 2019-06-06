class Singleton:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls, *args, **kwargs)
        return cls._instance


class MyClass(Singleton):
    pass


s = MyClass()
s2 = MyClass()
print(id(s) == id(s2))


class Singleton2(type):
    _instance = None

    def __call__(cls, *args, **kwargs):
        print('call')
        if cls._instance is None:
            cls._instance = super().__call__(*args, **kwargs)
        return cls._instance


class MyClass(metaclass=Singleton2):
    def __init__(self):
        super().__init__(self)
        print('init')

    def __new__(cls, *args, **kwargs):
        print('new')


print('-'*10)
s = MyClass()
print('-'*10)
s2 = MyClass()
print(id(s) == id(s2))

print('-'*10)
i = 0
print(i+1)
