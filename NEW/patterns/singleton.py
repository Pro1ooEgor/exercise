# Singleton v.1
class Singleton1:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls, *args, **kwargs)
        return cls._instance


print(Singleton1() is Singleton1())
instance1 = Singleton1()
instance2 = Singleton1()
instance1.foo = 'bar'
print(instance2.foo)


print('-'*10)
# Singleton v.2
class Singleton(type):
    _instance = None

    def __call__(cls, *args, **kwargs):
        print(cls._instance)
        if cls._instance is None:
            cls._instance = super().__call__(*args, **kwargs)
        return cls._instance


class MyClass(metaclass=Singleton):
    pass


a = MyClass()
b = MyClass()
print(id(a) == id(b))
b.x = 'foo'
print(a.x)
