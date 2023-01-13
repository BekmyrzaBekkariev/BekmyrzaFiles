
# [ Массивы ]

# 1. Удаления элемента списка во время его итерирования

# list_1 = [1, 2, 3, 4]
# list_2 = [1, 2, 3, 4]
# list_3 = [1, 2, 3, 4]
# list_4 = [1, 2, 3, 4]

# # Вариант 1
# for i, item in enumerate(list_1):
#     del item

# print(list_1)

# # Вариант 2
# for i, item in enumerate(list_2):
#     list_2.remove(item)

# print(list_2)

# # Вариант 3
# for i, item in enumerate(list_3):
#     list_3.pop(i)

# print(list_3)

# # Вариант 4
# for i, item in enumerate(list_4[:]):
#     list_4.remove(item)

# print(list_4)


# Крестики-нолики, где х побеждает с первой попытки

# row = [''] * 3
# board = [row] * 3
# print(board)

# board[0][0] = 'X'
# print(board)

# board = [[''] * 3 for _ in range(3)]
# board[0][0] = 'X'
# print(board)


# Те же операнды но другая история

# a = [1, 2, 3, 4]
# b = a
# a = a + [5, 6, 7]
# print(a, b)

# a = [1, 2, 3, 4]
# b = a
# a += [5, 6, 7]
# print(a, b)

# Игла в стоке сена

# t = ('one', 'two')
# for i in t:
#     print(i)

t = ('one')
for i in t:
    print(i)

t = ('one',)
for i in t:
    print(i)

# 5 Сохранить уникальные элементы

lst = [1, 3, 5, 7, 4, 3, 6, 2, 5, 3, 2, 4]
lst = list(set(lst))
print(lst)

# 6 Ключ словоря - изменяемый обьект

set_x = {1, 2, 3, }
lst_x = [1, 4, 9]

dict_x = {frozenset(set_x): lst_x}
dict_y = {tuple(lst_x): set_x}
