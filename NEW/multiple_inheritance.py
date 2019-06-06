class Person:
    animal_bool = False

    def __init__(self, name, age):
        self._name = name
        self.__age = age


class Animal:
    animal_bool = True

    def __init__(self, type_):
        self.animal_type = type_

    def calc(self):
        return 2


class World(Animal, Person):
    animal_bool = False

    def __init__(self):
        super().__init__('Hello')


w = World()
print(w.animal_bool)
