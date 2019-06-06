import pprint


class Person:
    howdy = 'Hi, bro'

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def hello(self):
        self.hi = 'hi'


pprint.pprint(dir(Person))  # class attributes:  howdy, hello

pprint.pprint(dir(Person('Egor', 22)))  # the attributes of the instance:
# howdy, hello, age, name

a = Person('Egor', 22)
a.hello()
pprint.pprint(dir(a))  # the attributes of the instance with attribute,
# that define in method hello: howdy, hello, age, name, hi
