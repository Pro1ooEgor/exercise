from functools import reduce
_sum = reduce((lambda x, y: x + y), [1, 2, 3, 4])  # 10
print(_sum)
# конечно, гораздо лучше воспользоваться sum:
_sum = sum([1, 2, 3, 4])  # 10
print(_sum)


alist = [(2, 2, 3), (1, 1), (1, 3, 3, 4)]
alist = sorted(alist, key=lambda x: x[0])
# сортируем по первому элементу в tuple
print(alist)  # [(1, 1), (1, 3, 3, 4), (2, 2, 3)]
