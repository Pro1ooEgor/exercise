from random import randint


class Base:
    def __init__(self, price, number):
        self.price = price
        self.numver = number

    @staticmethod
    def foo(variable):
        return 2 * randint(5, 10) - variable

    def foo_second(self, variable):
        return 2 * randint(5, 10) - variable


b = Base(2000, 123)
# Use staticmethod without creat instance of the class Base
print(Base.foo(2))


class Second:
    def __init__(self, a):
        self.a = a

    @classmethod
    def foo(cls):
        a = 10


s = Second(111)
print(s.a)
