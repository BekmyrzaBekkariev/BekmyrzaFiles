#  Разворот массива, Сортировка по умолчанию, сортировка сложных структур

import random

size = 10
array = [i for i in range(size)]
random.shuffle(array)
print(array)


# revers - функци разворота масива и сама функция снизу
def revers(array):
    for i in range(len(array) // 2):
        array[i], array[len(array) - i -
                        1] = array[len(array) - i - 1], array[i]


revers(array)
print(array)

# И у него есть метод  .revers()
array.reverse()
print(array)


# И есть метод сортировки снизу верх   .sort()

array.sort()
print(array)


# Сортировка Кортежей для него не поможет метод .sort()

print('*' * 50)

t = tuple(random.rendint(0, 100) for _ in range(size))
print(t)

# есть функция для кортеджа
# reverse=True
t = tuple(sorted(t, reverse=True))
print(t)
