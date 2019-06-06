import math


class Round:
    def __init__(self, radius):
        self.radius = radius
        self._square = None

    def calc_square(self):
        self._square = math.pi * self.radius

    def __get__(self):
        return self._square

    def __set__(self, instance, value):
        assert value >= 0
        self._square = value

    def __delete__(self, instance):
        del self._square


krg = Round(3)
krg.calc_square()
print(krg._square)
krg._square = 27
print(krg._square)
del krg._square
# print(krg._square)
