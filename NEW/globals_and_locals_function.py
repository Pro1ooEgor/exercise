def foo():
    x = 'some'
    print(globals())
    print(locals())

    def foo2():
        print('-' * 10)
        print(globals())
        print(locals())

    foo2()


foo()
