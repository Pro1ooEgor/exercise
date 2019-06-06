import math


class Round:
    def __init__(self, radius):
        self.radius = radius
        self._square = None

    def calc_square(self):
        self._square = math.pi * self.radius

    @property
    def square(self):
        return self._square

    @square.setter
    def square(self, value):
        self._square = value

    @square.deleter
    def square(self):
        del self._square


krg = Round(3)
krg.calc_square()
print(krg.square)
krg.square = 5
print(krg.square)
del krg.square
krg.square = 6
print(krg.square)

