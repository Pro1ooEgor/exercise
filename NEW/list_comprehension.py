# without anything
example_list = [i for i in range(5)]
print(example_list)  # [0, 1, 2, 3, 4]

# only if condition
example_list = [i for i in range(5) if i % 2 != 0]  # odd number
print(example_list)  # [1, 3]

# if-else condition
example_list = [i if i % 2 != 0 else i+1 for i in range(5)]
print(example_list)  # [1, 1, 3, 3, 5]

# with changing i
example_list = [i*2 for i in range(5)]
print(example_list)  # [0, 2, 4, 6, 8]


# range function
# range(start, stop, step)
# range(from includes, to not include, step)
# result: list in reverse
example_list = [i for i in range(5, 0, -1)]
print(example_list)  # [5, 4, 3, 2, 1]


# iteration over two lists with if condition x != y
example_list = [(x, y) for x in range(1, 5) for y in range(5, 1, -1) if x != y]
print(example_list)  # [(1, 5), (1, 4), (1, 3), (1, 2), (2, 5), (2, 4),
# (2, 3), (3, 5), (3, 4), (3, 2), (4, 5), (4, 3), (4, 2)]


# disclosure the list of lists - раскрытие списка списков
vec = [[[1, 2, 3], [4, 5, 6], [7, 8, 9]], [[10, 11, 12], [13, 14, 15], [16, 17, 18]]]
print([digit for lst in vec for elem in lst for digit in elem])
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]

# zip - joins into tuples what was transferred
print([(key, value) for (key, value) in zip([1, 2, 3], ['a', 'b', 'c'])])
# [(1, 'a'), (2, 'b'), (3, 'c')]
# dict - turning into a dictionary
print(dict([(key, value) for (key, value) in zip([1, 2, 3], ['a', 'b', 'c'])]))
# {1: 'a', 2: 'b', 3: 'c'}
# dictionary generator
print({key: value for key, value in zip([1, 2, 3], ['a', 'b', 'c'])})
# {1: 'a', 2: 'b', 3: 'c'}
# set generator
print({value for value in ['a', 'b', 'c']})
# {1: 'a', 2: 'b', 3: 'c'} - <class 'set'>


# generator
gen = (x for x in range(2))
print(gen)  # <generator object <genexpr> at 0x035CFE70>
print(gen.__next__())  # 0
print(next(gen))  # 1
try:
    next(gen)  # StopIteration
except StopIteration:
    print('StopIteration')

matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
]
print([[row[i] for row in matrix] for i in range(4)])


# ----
A0 = dict(zip(('a', 'b', 'c', 'd', 'e'), (1, 2, 3, 4, 5)))
# {'a': 1, 'c': 3, 'b': 2, 'e': 5, 'd': 4}
A1 = range(0, 10)  # range(0, 10)
A2 = sorted([i for i in A1 if i in A0])  # []
A3 = sorted([A0[s] for s in A0])  # [1, 2, 3, 4, 5]
print(A3)
