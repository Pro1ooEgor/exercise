test_list = [i for i in range(10)]
print(list(filter(lambda x: x % 2 == 1, test_list)))

print(list(map(lambda x: x**2, test_list)))

for i, value in enumerate(range(10, 50, 5)):
    print(i, value)

print(id(test_list))
test_list.append('hello')

# interesting
print(list(zip(
    [1, 2, 3, 4, 5],
    ('Hello', 'Tom', 'world'),
    {'yes', 'no'},
    {'key': 'value', 'key2': 'value2'}.values()
)))
