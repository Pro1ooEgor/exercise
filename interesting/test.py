def queue_time(customers, n):
    tills = [0] * n
    print(tills)
    for i in customers:
        print(tills)
        tills[0] += i
        tills.sort()
    return max(tills)


print(queue_time([10, 2, 3, 4, 5], 2))
