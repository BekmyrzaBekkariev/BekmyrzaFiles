
# [ Массивы ]

# 1. Удаления элемента списка во время его итерирования

list_1 = [1, 2, 3, 4]
list_2 = [1, 2, 3, 4]
list_3 = [1, 2, 3, 4]
list_4 = [1, 2, 3, 4]

# Вариант 1
for i, item in enumerate(list_1):
    del item

print(list_1)

# Вариант 2
for i, item in enumerate(list_2):
    list_2.remove(item)

print(list_2)

# Вариант 3
for i, item in enumerate(list_3):
    list_3.pop(item)

print(list_3)
# Вариант 4
for i, item in enumerate(list_4[:]):
    list_4.remove(item)

print(list_4)


# Крестики-нолики, где х побеждает с первой попытки
