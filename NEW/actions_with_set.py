a = [1, 2, 3, 4, 5]
b = [10, 8, 6, 4, 2]

a = set(a)
b = set(b)

print(a | b)  # объединение
print(a.union(b))

print(a & b)  # пересечение (и там, и там)
print(a.intersection(b))

print(b - a)  # разница (всё что есть в b минус то, что есть в а)
print(a.difference(b))
print(a - b)

print('cимметричная разница')
print(a ^ b)  # cимметричная разница - все элементы a и b, за исключением общих
print(a.symmetric_difference(b))

months_a = {"Jan", "Feb", "March", "Apr", "May", "June"}
months_b = {"Jan", "Feb", "March", "Apr", "May", "June", "July", "Aug", "Sep",
            "Oct", "Nov", "Dec"}

subset_check = months_a.issubset(months_b)
superset_check = months_b.issuperset(months_a)

print(subset_check)
print(superset_check)

months_a = {"Jan", "Feb", "March", "Apr", "May", "June"}
months_b = {"Jan", "Feb", "March", "Apr", "May", "June", "July", "Aug", "Sep",
            "Oct", "Nov", "Dec"}

subset_check = months_a <= months_b  # является частью B (дочернее, ребёнок)
superset_check = months_b >= months_a  # включается в себя A (родитель)

print(subset_check)  # True
print(superset_check)  # True

subset_check = months_a.issubset(months_b)
superset_check = months_b.issuperset(months_a)

print(subset_check)  # True
print(superset_check)  # True
