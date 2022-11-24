# import random
# number = random
# running = True

# while running:
#     guess = int(input('Введите целое число : '))
#     if guess == number:
#         print('Поздравляю, вы угадали.')
#         running = False # это останавливает цикл while
#     elif guess < number:
#         print('Нет, загаданное число немного больше этого')
#     else:
#         print('Нет, загаданное число немного меньше этого.')
# else:
#     print('Цикл while закончен.')
#     # Здесь можете выполнить всё что вам ещё нужно
# print('Завершение.')

# for i in range(1,6):
#     print(i)
# else:
#     print('Цикл закончен')

# while True:
#     s = input('Введите что-нибудь : ')
#     if s == 'выход':
#         break
#     print('Длина строки: ', len(s))
# print('Завершение')

# while True:
#     s = input('Введите что-нибудь : ')
#     if s == 'выход':
#         break
#     if len(s) < 3:
#         print('Слишком мало')
#         continue
#     print('Введённая строка достаточной длины')
# # Разные другие действия здесь...


# def sayHello():
#     print('Привет, Мир!') # блок, принадлежащий функции
# # Конец функции
# sayHello() # вызов функции
# sayHello() # ещё один вызов функции

# Function
# def printMax(a, b):
#     if a > b:
#         print(a, 'максимально')
#     elif a == b:
#         print(a, 'равно', b)
#     else:
#         print(b, 'максимально')
        
# printMax(3, 4) # прямая передача значений

# x = 5
# y = 7

# printMax(x, y) # передача переменных в качестве аргументов

# x = 50 

# def func(x):
# 	print('х равен', x)
# 	x = 2
# 	print('Замена локального х на ' , x )


# func(x)
# print('х по прежнему', x)


# def say(massage, time = 1):
# 	print(massage * time)

# say('Hello')
# say('Hello', 4)

#Модули

# import sys

# print('Аргументы командной строки:')
# for i in sys.argv:
#     print(i)
    
# print('\n\nПеременная PYTHONPATH содержит', sys.path, '\n')

# if __name__ == '__main__':
# 	print('Эта программа запущена сама по себе.')
# else:
# 	print('Меня импортировали в другой модуль.')

# def sayhi():
# 	print('Привет! Это говорит мой модуль.')
 
# __version__ = '0.1'

