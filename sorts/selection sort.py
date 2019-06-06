# O(n2)
# сортировка выбором
# В неотсортированном подмассиве ищется локальный минимум.
# Найденный минимум меняется местами с первым элементом в подмассиве.
# Если в массиве остались неотсортированные подмассивы — смотри пункт 1.


def selection(data):
    for i, e in enumerate(data):
        mn = min(range(i, len(data)), key=data.__getitem__)
        data[i], data[mn] = data[mn], e
    return data


li = [6, 5, 3, 1, 8, 7, 2, 4]
print(selection(li))
