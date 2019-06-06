age = 35
print(age.__class__)
name = 'Bob'
print(name.__class__)
def foo(): pass
print(foo.__class__)
class Bar: pass
b = Bar()
print(b.__class__)
print(type(Bar))


class A:
    qux = 'A'

    def __init__(self, name):
        self.name = name

    def foo(self):
        print('foo')


a = A('a')
print(a.__class__)
print(a.__dict__)
print(dict(A.__dict__))
print(dir(a))
print(dir(A))

print(isinstance(A, type))
print(isinstance(43, type))

# type(name=, bases=, dict=)
print(A.__name__)
print(A.__bases__)
print(dict(A.__dict__))
print(A.__class__)
