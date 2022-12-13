# 2.2 Рекурсивные Алгоритмы
def func(a, b):
    if a == b:
        return f'{a}'
    if a > b:
        return f'{a}, {func(a - 1, b)}'
    if a < b:
        return f'{a}, {func(a + 1, b)}'


print(func(1, 10))

# Мой пример


def func(a, b):
    if a == b:
        return f'{a}'
    if a > b:
        return f'{a}, {func(a - 1, b)}'
    if a < b:
        return f'{a}, {func(a + 1, b)}'


a = int(input())
b = int(input())
print(func(a, b))
