li = [0, 3, 5, 7, 10, 20, 28, 30, 45, 56]
x = 56
i = 0
j = len(li) - 1
m = int(j / 2)
ii = 0
while li[m] != x and i < j:
    if x > li[m]:
        i = m + 1
    else:
        j = m - 1
    m = int((i + j) / 2)
    ii+=1
    print(ii)

if i > j:
    print('Элемент не найден')
else:
    print('Индекс элемента: ', m)