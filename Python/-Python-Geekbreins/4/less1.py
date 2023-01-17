# timeit - это биб для измерение времени

# import timeit
# x = 2 + 2
# print(timeit.timeit('x = 2 + 2'))
# print(timeit.timeit('x = sum(range(10))'))

# cProfile - это биб для тоже измерение времени
import cProfile


def get_len(array):
    return len(array)


def get_sum(array):
    s = 0
    for i in array:
        s += i
    return s


def main():
    lst = [i for i in range(100)]
    a = get_len(lst)
    b = get_sum(lst)


# команда котороя показывает
cProfile.run('main()')
