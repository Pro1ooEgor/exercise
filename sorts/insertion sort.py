# O(n2)
# сортировка вставками
# Перебираются элементы в неотсортированной части массива.
# Каждый элемент вставляется в отсортированную часть массива на то место,
# где он должен находиться.


def insertion(data):
    for i in range(len(data)):
        j = i - 1  # previous index
        key = data[i]
        # key - current element
        # data[j] - previous element
        while data[j] > key and j >= 0:
            data[j + 1] = data[j]  # set current elem equal previous
            j -= 1
        data[j + 1] = key  # now we found place, where need to set current element
        print(data)
    return data


li = [6, 5, 3, 1, 8, 7, 2, 4]
print(f'result: {insertion(li)}')
