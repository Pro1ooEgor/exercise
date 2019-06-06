def transpose_list(list_of_lists):
    return [list(row) for row in zip(*list_of_lists)]


def transpose_list_2(list_of_lists):
    return [row for row in zip(*list_of_lists)]


# print(transpose_list([[1, 4, 7], [2, 5, 8], [3, 6, 9]]))
# print(transpose_list_2([[1, 4, 7], [2, 5, 8], [3, 6, 9]]))

# fruits = ["apple", "banana", "cherry"]
# for x in fruits:
#     print(x) if x != "banana" else print


def with_previous(iterable, *, fillvalue=None):
    """Yield each iterable item along with the item before it."""
    previous = fillvalue
    for item in iterable:
        yield previous, item
        previous = item


# print(list(with_previous([2, 1, 3, 4], fillvalue=0)))

fruits = ['lemon', 'pear', 'watermelon', 'tomato']
# first, second, *remaining = fruits
first, *middle, last = fruits
# print(middle)

fruits = ['lemon', 'pear', 'watermelon', 'tomato']
((first_letter, *remaining), *other_fruits) = fruits
# print(remaining)


def palindromify(sequence):
    return [*sequence, *reversed(sequence)]


def rotate_first_item(sequence):
    return [*sequence[1:], sequence[0]]


print(rotate_first_item(fruits))
