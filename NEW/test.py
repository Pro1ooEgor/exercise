alist = [1, 2, 3, 4, 5]
print(list(reversed(alist)))


class SimpleIterator:
    def __init__(self, limit):
        self.curr = 0
        self.limit = limit

    def __iter__(self):
        return self

    def __next__(self):
        if self.curr < self.limit:
            self.curr += 1
            return self.curr
        else:
            raise StopIteration


s = SimpleIterator(3)
print(next(s))

for i in s:
    print(i)


def gen(limit):
    prev, next = 0, 1
    while prev < limit:
        yield prev
        prev, next = next, prev + next


g = gen(10)
for i in g:
    print(i)


def decorator(func):
    def wrapper():
        print('До')
        func()
        print('После')
    return wrapper


@decorator
def test_func():
    print('In the middle')


test_func()


print(list(zip(
    [1, 2, 3, 4, 5],
    ('Hello', 'Tom', 'world'),
    {'yes', 'no'},
    {'key': 'value', 'key2': 'value2'}.values()
)))

print(list(filter(lambda x: x > 10, [1, 2, 5, 10, 50, 100])))
print(list(map(lambda x: x > 10, [1, 2, 5, 10, 50, 100])))
print(list(map(lambda x: x + 10, [1, 2, 5, 10, 50, 100])))

print([i for i in range(10) if i % 2 == 0])

a = [1, 2, 3, 4, 5]
b = [10, 8, 6, 4, 2]

a = set(a)
b = set(b)

print(a.union(b))
print(a.intersection(b))
print(a.difference(b))

print(a | b)
print(a & b)
print(a - b)


# Даны 2 массива, надо найти их общие элементы;
# те, которые есть в 1 массиве и нет в другом

mas1 = [1, 2, 3, 4, 5, 6]
mas2 = [2, 4, 6, 8]
mas1 = set(mas1)
mas2 = set(mas2)

print('result: ' + str(mas1 & mas2))
print('result: ' + str(mas1 - mas2))

# Даны 1000 элементов, как сделать список с только нечетными элементами

li = [i for i in range(1000) if i % 2 == 0]

