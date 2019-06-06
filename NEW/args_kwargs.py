def person_info(name, *args):
    result_string = name
    for i in args:
        result_string += ' ' + str(i)
    return result_string


print(person_info('Alexa', 23, 'Grodno', 29))

example_list = ['Hello', 'World', 12, 23]

print(person_info('Alexa', *example_list))


def person_info(name, **kwargs):
    result_string = f'Name: {name}'
    for key, value in kwargs.items():  # an iteration over the dictionary
        result_string += f', {key}: {value}'
    return result_string


print(person_info('Alexa', age=12, city='Moscow'))
