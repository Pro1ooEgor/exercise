def queue_time(queue_of_people, number_of_register):

    result = 0

    def movement_of_the_queue(registers: list, result: int):
        min_register = min(registers)
        result += min_register
        for i in range(len(registers)):
            registers[i] -= min_register
            if registers[i] == 0:
                registers[i] = 'free'
        return registers, result

    list_of_register = []
    for n in range(number_of_register):
        list_of_register.append('free')
    print(list_of_register)
    for man in queue_of_people:
        for i in range(len(list_of_register)):
            print(list_of_register)
            if list_of_register[i] == 'free':
                list_of_register[i] = man
                break
            elif 'free' not in list_of_register:
                _, result = movement_of_the_queue(list_of_register, result)

    print(list_of_register)

    return result + max(list_of_register)


print(queue_time([5, 3, 4], 1))
print(queue_time([10, 2, 3, 3], 2))
print(queue_time([2, 3, 10], 2))
