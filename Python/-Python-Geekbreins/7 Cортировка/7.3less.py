# Сортировка с Вставками

import random

size = 10
array = [i for i in range(size)]
random.shuffle(array)
print(array)


def insertion_sort(array):

    for i in range(1, len(array)):
        spam = array[i]
        j = 1

        while array[j - 1] > spam and j > 0:
            array[j] = array[j - 1]
            j -= 1

        array[j] = spam
        # print(array) Можно увидить как движется


insertion_sort(array)
print(array)
