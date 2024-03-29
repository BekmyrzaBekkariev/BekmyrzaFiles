# 3. Написать программу, которая генерирует в указанных пользователем границах:
# a. случайное целое число,
# b. случайное вещественное число,
# c. случайный символ.
# Для каждого из трех случаев пользователь задает свои границы диапазона. Например, если надо получить случайный символ от 'a' до 'f', то вводятся эти символы. Программа должна вывести на экран любой символ алфавита от 'a' до 'f' включительно.
import random

num_start = input('Начало диапозона: ')
num_end = input('Конец диапозона: ')
choice = input(
    'Ведите номер действия:\n1. Случайное целое число\n''2. Cлучайное вещественное число\n3.Слуйсайный символ\n')

if choice == '1':
    print('Случайное целое число')
    num_start = int(num_start)
    num_end = int(num_end)
    result = random.randint(num_start, num_end)

elif choice == '2':
    print('Cлучайное вещественное число')
    num_start = float(num_start)
    num_end = float(num_end)
    result = random.uniform(num_start, num_end)

elif choice == '3':
    print('Слуйсайный символ')
    num_start = ord(num_start)
    num_end = ord(num_end)
    result = chr(random.randint(num_start, num_end))

else:
    result = 'Неизвестное действие'

print(result)
