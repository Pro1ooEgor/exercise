authors = ['Настя', 'Вика', 'Олег', 'Иванушки интернешенел']
titles = ['Мой любимый', 'Только ты один у меня', 'ЛСП', 'Тополиный пух']

example_list = []

unique_index = 1
for author, title in zip(authors, titles):
    example_list.append((unique_index, author, title))
    unique_index += 1

# print(list(enumerate(example_list)))
#
# for index, value in enumerate(example_list):
#     print(index, value)

for i in example_list:
    print(i)

