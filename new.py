pairs = [(4, 11), (8, 8), (5, 7), (11, 3)]
sorted_by_smallest = sorted(pairs, key=lambda items: min(items))
print(sorted_by_smallest)

pairs = [(4, 11), (8, 8), (5, 7), (11, 3)]
sorted_by_smallest2 = sorted(pairs, key=min)
print(sorted_by_smallest2)

print(list(map(lambda items: items[1], pairs)))

my_dict = {'a': 3, 'c': 1, 'b': 2}
# Упорядочим элементы словаря по ключам.
sorted(my_dict.items(), key=lambda item: item[0])
# [('a', 3), ('b', 2), ('c', 1)]

my_dict = {'a': 3, 'c': 1, 'b': 2, '0': 3}

# Упорядочим элементы словаря по значениям.
print(sorted(my_dict.items(), key=lambda item: (item[0])))
# [('c', 1), ('b', 2), ('a', 3)]

my_dict = {'a': 3, 'c': 1, 'b': 2, '0': 3}

# Упорядочим по значениям и ключам.
sorted(my_dict.items(), key=lambda item: (item[1], item[0]))
# [('c', 1), ('b', 2), ('0', 3), ('a', 3)]

# А теперь по значениям по убыванию и ключам.
sorted(my_dict.items(), key=lambda item: (-item[1], item[0]))
# [('0', 3), ('a', 3), ('b', 2), ('c', 1)]


def length_and_alphabetical(string):
    return (len(string), string.casefold())


colors = ["Goldenrod", "Purple", "Salmon", "Turquoise", "Cyan"]
colors_by_length = sorted(colors, key=length_and_alphabetical)
print(colors_by_length)
