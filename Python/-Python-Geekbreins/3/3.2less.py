# Бинарный поиск !!! 90% програмистов не могут написать этот код!
# Короче писк который показывает индекс числа в мамссиве


import random


def bin_search(array, value):
    left = 0
    right = len(array) - 1
    pos = len(array) // 2
    while array[pos] != value and left <= right:
        if value > array[pos]:
            left = pos + 1
        else:
            right = pos - 1

        pos = (left + right) // 2

    return -1 if left > right else pos

# Вместо -1 можно написать None


a = [random.randint(0, 1000) for _ in range(100)]
a.sort()
print(a)

n = int(input('Какой элемент найти: '))
print(bin_search(a, n))
