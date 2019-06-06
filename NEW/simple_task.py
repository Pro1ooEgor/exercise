from random import randint

exaple_list = [i for i in range(100) if i % randint(5, 10) == 0]

print(exaple_list)
print(min(exaple_list))
print(max(exaple_list))
print(exaple_list[10:2:-1])

a = [1, 2, 2, 3, 4, 5, 5, 5]
a = list(set(a))
print(a)
print(type(a))

###

test_string = 'Hello world i have learned python look at this'
print(max(test_string.split()))
large = 0
# result = ''
for i in test_string.split():
    if len(i) > large:
        result, large = i, len(i)

print(f'large: {large}, word: {result}')

my_list = [1, 2, 3, 4]

new_list = my_list.copy()
new_list.append(5)
print(my_list)
print(new_list)

new_new_list = my_list[:]
new_new_list.append(10)
print(my_list)
print(new_new_list)
