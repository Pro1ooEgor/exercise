# O(n log n)
# divide and conquer
# Сортируемый массив разбивается на две части примерно одинакового размера;
# Каждая из получившихся частей сортируется отдельно, например —
# тем же самым алгоритмом;
# Два упорядоченных массива половинного размера соединяются в один.


# Code for the merge subroutine
def merge(a, b):
    """ Function to merge two arrays """
    c = []
    while len(a) != 0 and len(b) != 0:
        if a[0] < b[0]:
            c.append(a.pop(0))
        else:
            c.append(b.pop(0))
    if len(a) == 0:
        c += b
    else:
        c += a
    return c


# Code for merge sort
def mergesort(data):
    """ Function to sort an array using merge sort algorithm """
    if len(data) == 0 or len(data) == 1:
        return data
    else:
        middle = len(data) // 2
        a = mergesort(data[:middle])
        b = mergesort(data[middle:])
        return merge(a, b)


li = [6, 5, 3, 1, 8, 7, 2, 4, 9]
print(mergesort(li))

