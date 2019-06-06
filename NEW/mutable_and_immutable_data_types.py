def foo(string):
    return string + '!'


# number, string, tuple, boolean immutable
petya = 'Petya'
print(foo(petya))
print(petya)


def foo(dict, kword):
    dict[kword] = "Petya"
    return dict


# dictionary, list, set mutable (transmitted by reference)
example_dict = {'name': 'Vasya'}
print(example_dict)
print(foo(example_dict, 'name'))
print(example_dict)


def foo_set(input_set):
    input_set.add('hello')


input_set = {1, 2, 3}
foo_set(input_set)
print(input_set)

# динамическая типизация python
i = 'string'
print(type(i))
i = 123
print(type(i))


# tuple - кортёжь.
# Нельзя добавлять .append или изменять по индексу [0] = 'something'
t = ('Hello', 'world', 1)


