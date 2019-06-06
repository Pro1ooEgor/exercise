from random import random


def array(a):
    s = 0
    for i in range(15):
        a[i] = int(random() * 50)
        print("%4d" % a[i], end='')
        s += a[i]
    print(" - %d" % s)
    return s


arr_new = [0] * 15
print(arr_new)
sum_max = 0
for i in range(10):
    sum_new = array(arr_new)
    if sum_new > sum_max:
        sum_max = sum_new
        index = i + 1
        arr_max = arr_new

print("%d-й массив имеет максимальную сумму элементов:" % index)
print(arr_max, ' - ', sum_max)
