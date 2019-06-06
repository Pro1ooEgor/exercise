example_list = [1, 2, 'Hello']

itr = iter(example_list)
print(next(itr))  # 1
print(next(itr))  # 2
print(next(itr))  # Hello
# print(next(itr))  # StopIteration


class SimpleIterator:
    def __init__(self, limit):
        self.limit = limit
        self.counter = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.counter < self.limit:
            self.counter += 1
            return self.counter
        else:
            raise StopIteration


exp_itr = SimpleIterator(2)
# print(next(exp_itr))  # 1
# print(next(exp_itr))  # 2
# print(next(exp_itr))  # StopIteration

for i in exp_itr:
    print(i)
# 1, 2
# without StopIteration. The program does not break
# Because there is __iter__ method in the SimpleIterator class


# generator
def simple_generator(val):
    while val > 0:
        val -= 1
        yield val


gen_iter = simple_generator(5)
print('-'*10)
print(next(gen_iter))  # 4
print(next(gen_iter))  # 3
print(next(gen_iter))  # 2
print(next(gen_iter))  # 1
print(next(gen_iter))  # 0
# print(next(gen_iter))  # StopIteration

from itertools import islice


class fib:
    def __init__(self):
        self.prev = 0
        self.curr = 1

    def __iter__(self):
        return self

    def __next__(self):
        value = self.curr
        self.curr += self.prev
        self.prev = value
        return value


f = fib()
print(list(islice(f, 0, 10)))
# [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]


def fib():
    prev, curr = 0, 1
    while True:
        yield curr
        prev, curr = curr, prev + curr


f = fib()
print(list(islice(f, 0, 10)))
# [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]


# generator
def gen(start, stop):
    while start < stop:
        yield start
        start += 1


g = gen(0, 10)
print(g.__next__())  # 0
print(next(g))  # 1
print(list(g))  # [2, 3, 4, 5, 6, 7, 8, 9]


def gen():
    print('Начало')
    for i in range(3):
        print('шаг ' + str(i))
        yield i
    return 'The end'


print('-'*5)
g = gen()
print(next(g))
print(next(g))
print(next(g))
print(next(g))  # StopIteration: The end
