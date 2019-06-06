x = 20


def my_func(a, b):
    x = 10

    def func2():
        global x
        x *= 2
        print(x)

    func2()


my_func(1, 2)
print(x)  # 40

x = 20


def my_func(a, b):
    x = 10

    def func2():
        nonlocal x
        x *= 2
        print(x)  # 20

    func2()


my_func(1, 2)
print(x)
