# $$-------Грокаем Алгитмы-------$$
# def binary_search(list, item):
# 	low = 0
# 	high = len(list)-1
# 	while low <= high:
# 		mid = (low + high)
# 		guess = list[mind]
# 		if guess == item:
# 			return mid
# 		if guess > item:
# 			high = mid - 1
# 		else:
# 			low=mid+1
# 	return None
# my_list = [1,3,5,7,9]
# print binary_search(my_list, 3)
# print binary_search(my_list, -1)
# import sys, warnings
# if sys.version_info[0] < 3:
# 	warnings.warn("Для выполнения этой программы необходима как минимум \
# 	версия Python 3.0",RuntimeWarning)
# else:
# 	print('Нормальное продолжение')
# Алгоритм массива по возростанию
# def Smallest(arr):
#     smallest = arr[0]
#     smallest_index = 0
#     for i in range(1, len(arr)):
#         if arr[i] < smallest:
#             smallest = arr[i]
#             smallest_index = i
#         return smallest_index
# Использования этого алгоритма
# def selection(arr):
#     newArr = []
#     for i in range(len(arr)):
#         smallest = smallest(arr)
#         newArr.append(arr.pop(smallest))
#     return newArr
# print(selection([5,3,6,2,10]))


# $$-------tess-------$$
# a = float ( input ('ведите значение основание'))
# h = float(input('ведите значение высоты'))
# s = a*h
# print ('ответ: s=',s)
# # a = 23
# # b = 7,5
# # c= 'hello'
# # print = (a,b,c)
# code = 1234567890
# a = int (input ('ведите десять кодов:'))
# while a != code:
#     print ('неверный код.ведите снова .')
#     a = int (input('ведите десять кодов:'))
#     if a == code:
#         print ('код веден верно')
#         print ('gjplhjdkz')
# -----------------
# a = int(input ('ведите числиеть первого числа: '))
# b = int(input ('ведите знаменатель первого числа: '))
# c = int(input ('ведите числиеть второго числа: '))
# d = int(input ('ведите знаменатель второго числа: '))
# print(a/b + c/d)
# --------------------------
# from fractions import Fraction
# a,b,c,d = map(int,input('''
#  Ведите числиеть первого числа
#  Ведите знаменатель первого числа
#  Ведите числиеть второго числа
#  Ведите знаменатель второго числа
#  >>> ''').split())
# v = (Fraction(a,b))
# b = (Fraction(c,d))
# print(v + b)
# ------------------------
# a = int(input ('ведите числиеть первого числа: '))
# b = int(input ('ведите знаменатель первого числа: '))
# ab = a / b
# print ('ответ ab=',ab )
# c = int(input ('ведите числиеть второго числа: '))
# d = int(input ('ведите знаменатель второго числа: '))
# cd = c / d
# print ('ответ:cd/ab',cd/ab)
# p=(a/b)+ (c/d)
# print ('ответ p= ',p )
# from turtle import*
# t = Turtle()
# bgcolor('black')
# t.pencolor('green')
# t.speed(0)
# for i in range(340):
#     t.circle(190-i,90)
#     t.left(90)
#     t.circle(190-i,90)
#     t.left(18)
#     if i > 190:
#         t.pensize(3)
# mainloop()
# import random
# what = input('что узнать?:')
# i = 0
# for proc in range(101):
#     print ('думаем ',i,'%')
#     i +=1
# print()
# a = ['да','нет','возможно','не знаю','не обязан']
# print (what,':',random.choice(a))
# print('\n\n')
# print ("Общество в начале XXI века")n
# a = int(input("Ваш возрост"))
# if a<=7:
#     print ("Вам в детский сад")
# elif a > 18 or a < 25:
#     print ("Вам в профессиональное учебное заведение")
# elif a > 25 or a < 60:
#     print ("Вам на работу")
# elif a > 60 or a < 120:
#     print ("Вам предоставляется выбор")
# elif a < 0 or a > 120:
#     while i < 5:
#         i = i + 1
#         print (i)
# def qualifier(a):
#     if 0<=a<7:
#         print("Детский сад")
#     elif 7<=a<=18:
#         print("Школа")
#     elif 19<=a<25:
#         print("Проф. образование")
#     elif 25<=a<60:
#         print("Работа")
#     elif 60<=a<=120:
#         print("вам предостовляет выбор")
#     elif a<0 or a>120:
#         print("НЛО")
# print('Общество в начале XXI века')
# user_old= int(input('Сколько вам лет? '))
# qualifier(user_old)

# $$-------zadacha-------$$
# Задача №1
# С клавиатуры вводятся 2 целых числа a и b.Нужно вывести все
# числа в дапозоне от a и b, а так же указать кол-во этих чисел.

#a = int(input())
#b = int(input())
#q = 0
# for a in range(a,b+1):
#    print(a)
#    q=q+1
#print('Кол-во чисел:',q)
# Задача №2
# Дано вещественное число, стоимость 1 кг конфет.
# Вывести стомость 1,2...10кг конфет.
# b = int(input("стоимость"))
# cost = 0
# for a in range(1,11):
#     cost= b*a
#     print('Cтоимость',a,'кг. конфет = ',cost)
# Задача №3
# Пользователь вводит кол-во чисел в последовательности, а затем
# сами числа. Программа выводит сумму всех отрицательных чисел.
# a = int(input())
# su = 0
# for a in range(1,a+1):
#     b = int(input())
#     if b<0:
#         su=su+b
# print(su)
# Задача №4
# Пользователь вводит 3 целых числа.Найти кол-во
# положительных чисел. Вести на экран
# q = 0
# a = int(input())
# if a > 0:
#     q = q + 1
# a = int(input())
# if a > 0:
#     q = q + 1
# a = int(input())
# if a > 0:
#     q = q + 1
# print(q)
# Задача №5
# Пользователь вводит произвольное число. Если оно является
# положительным, то к нему прибовляется 1. Если число отрицательное,
# то от него вычитается 2. Результат выводится на экран.
# a = int(input())
# if a > 0:
# 	a = a + 1
# else:
# 	a = a - 2
# print(a)
# Задача №6
# Необходимо написать программу, которая в последовательности
# чисел определяет кол-во чисел больше 10.
# Прогамма работает по следушему алгоритму:
# Вы вводите с клавиатуры последовательность целых чисел.
# Их может быть неограничено кол-во.
# ввод чисел остановливаются числом 0.
# В конце работы программы выводится кол-во чисел со значением больше 10.
# a = int(input())
# q=0
# while a!=0:
# 	if a>10:
# 		q=q+1
# 	a=int(input())
# print(q)
# Задача №7
# Необходимо написать программу, которая в последовательности
# чисел определяет сумму всех положительных чисел.
# Прогамма работает по следушему алгоритму:
# Вы вводите с клавиатуры последовательность целых чисел.
# Их может быть неограничено кол-во.
# ввод чисел остановливаются числом 0.
# В конце работы программы выводится кол-во чисел со значением больше 10.
# a = int(input())
# su = 0
# while a!=0:
# 	if a>0:
# 		su=su+a
# 	a=int(input())
# print(su)
# Задача №8
# Напишите программу, которая в последовательности натуральных чисел
# определяет кол-во чисел, кратных 6 и оканчивающихся на 4. Прогамма
# получает на выход кол-во чисел в последовательности, а затем сами числа.
# Кол-во чисел не превышает 1000.Ведённые числа по модулю не превышают 30 000.
# Прогамма должна вывести одно число:кол-во чисел, кратных 6 и оканчивающихся на 4.
# a=int(input())
# q=0
# for b in range(0,a):
# 	a=int(input())
# 	if a%6==0 and a%10==4:
# 		q=q+1
# print(q)
# Задача №9
# Напишите программу котораяв последовательности целых чисел определяет их
# кол-во и сумму чётных чисел. Прогамма получает на выход целые числа, кол-во
# Ведённых чисел неизвестно, последовательность чисел заканчивается числоми 0
# (0-признак окончания ввода, не выходит в последовательность).
# Кол-во чисел не превышают 1000. Ведённые числа по модулю не превышают 30 000.
# Прогамма должна вывести два числа: длину последовательности и их сумму чётных чисел.
# a=int(input())
# su=0
# q=0
# while a!=0:
# 	if a%2==0:
# 		su=su+a
# 	q=q+1
# 	a=int(input())
# print(q)
# print(su)
# Задача №9
# Пользователь вводит кол-во чисел а затем сами числа.Все числа последовательности целые.
# Прогамма выводит весь список чисел и сумму положительных чисел.
# a=int(input())
# q=[0]*a
# s=0
# for i in range(a):
# 	q[i]=int(input())
# 	s=s+q[i]
# print(q)
# print('Сумма всех элементов =',s)

# $$-------HaydDi-------$$
# 1 день 1 задача
# from math import sqrt
# def dist2(xa, ya, xb, yb):
#     return (xa-xb)**2 + (ya-yb)**2
# x1, y1, x2, y2, x3, y3 = map(int, input().split())
# d = []
# d.append(dist2(x1, y1, x2, y2))
# d.append(dist2(x2, y2, x3, y3))
# d.append(dist2(x3, y3, x1, y1))
# d.sort()
# if sqrt(d[2]) == sqrt(d[0]) + sqrt(d[1]):
#     r = 'L'
# elif d[2] == d[0] + d[1]:
#     r = 'R'
# elif d[2] < d[0] + d[1]:
#     r = 'A'
# elif d[2] > d[0] + d[1]:
#     r = 'O'
# if (d[0] == d[1] or d[1] == d[2]) and d[0] != 0:
#     r = r + 'E'
# print(r)
# ########################
# 1 день 2 задача
# def sol(x):
#     return (a*x + b)*x == c
# def all_divs(n):
#     i=1
#     r=[]
#     while (i*i<=n):
#         if n%i == 0:
#             if sol(i):
#                 r.append(i)
#             if sol(-i):
#                 r.append(-i)
#             k = n//i
#             if i != k:
#                 if sol(k):
#                     r.append(k)
#                 if sol(-k):
#                     r.append(-k)
#         i += 1
#     return sorted(r)
# a, b, c = map(int, input().split())
# d = all_divs(c)
# print(d[0] if len(d) != 0 else 0)
# import math
# #===============================================================
# def get_int_eq_root(a, b, c):
#     D = b * b - 4 * a * c
#     if D < 0:
#         return 0
#     D_root = int( math.sqrt(D) )
#     if D_root * D_root != D:
#         return 0
#     res = -b - D_root
#     res, rem = divmod( res, 2 * a )
#     if rem:
#         return 0
#     return res
# #===============================================================
# while True:
#     print( 'Введите натуральные коэффициенты уравнения (А*X + B)*X = С:' )
#     a, b, c = map(int, input( 'A, B, C: ' ).split() )
#     print( get_int_eq_root(a,b,-c) )
#     print()

# 1 день 3 задача
# m, n = map(int, input().split())
# solutions = 0
# for x in range(2, n + 1):
#     for y in range(2, n + 1):
#         for z in range(2, n + 1):
#             if (7 * n - x - 2 * y - 4 * z) < m:
#                 solutions += 1
# print(solutions)
# a,b,c,d = map(int, input().split())
# def solve(a,b,c,m) : # split and solve
#     result = 1
#     p = 2            # primes
#     while p**2 <= a :
#         z = 0
#         while a % p == 0 :
#                      # calculate z
#             a /= p
#             z += 1
#         if z != 0 :
#             result *=  modpow(p,z,b,c,m)
#             result %= m
#         p += 1
#     if a != 1 :      # Possible last prime
#         result *= modpow(a, 1, b, c, m)
#     return result % m
#     print(solove(a,b,c,d))
# a,b,c,d,m = map(int,input().split())
# j = (a**b**c**d)%m
# print(j)
# -----------------------------
# def title_txt(string):
#     return string.title()
# print(title_txt(input()))
# def gcd(a,b):
#   while a != 0 and b !=0:
#     if a > b:
#       a = a % b
#     else:
#       b = b % a
#   return a+b
# q = map(int, input(a,b)
# --------------------------------
# import math
# print( math.gcd(30,18) )
# ---------------------------
#a = 'He;;0 wor1d'
#print( a[::-1] )
# --------------------------
# def read_ints():
#   return list(map(int,input().split()))
#   # return [int(i) for i in input().split() ]
# def read_int():
#   return read_ints()[0]
# n = read_int() + 1
# p = read_ints()
# a = read_ints()
# head = 0
# lefts = [-1]* n
# rights = [-1]* n
# def connect(left, right):
#   lefts[right] = left
#   rights[left] = right
# connect(p[n-1],p[0])
# for i in range(1,n):
#   connect(p[i-1],p[i])
# ans = [[-1,-1] for i in range(n-1)]
# for i in range(n-1):
#   child = a[i]
#   left,right = lefts[child],rights[child]
#   ans[i] = [left,right]
#   connect(left, right)
# print('\n'.join([' '.join([str(index) for index in neighbours]) for neighbours in ans]))
# -----------------------------------------
# def read_ints():
#   return list(map(int,input().split()))
# def read_int():
#   return read_ints()[0]
# candidates_count, cities_count = read_ints()
# votes = [
#   read_ints() for city in range(cities_count)
# ]
# candidate_wins = [0] * candidates_count
# def first_max_index(values):
#   res_index = 0
#   for i in range(len(values)):
#     if values[res_index] < values[i]:
#       res_index = i
#   return res_index
# for city_votes in votes:
#   winner = first_max_index(city_votes)
#   candidate_wins[winner] += 1
# president = first_max_index(candidate_wins)
# print(president + 1)
# #===============================
# w,h,n = map(int,input().split())
# xl = 1
# xr = h * n
# while xl + 1 <xr:
#   m=(xl+xr)/2
#   k = (m/w)*(m/h)
#   if k>=n:
#     xr=m
#   else:
#     xl=m
# print(int(xr))

# $$-------ZADACHI HACATON DUMAL-------$$
# Reversed String
# def solution (string):
#     result_sting = ''
#     for i in range (len(string)-1,-1,-1):
#         result_sting += string[i]
#     return result_sting
# print(solution("ssd"))

# Даны два символа если оба буквы то 1 если оба одного регистра то 1 если разного то 0
# def same_case(a,b):
#     if not a.isalpha() or not b.isalpha():
#         return -1
#     if not a.isupper() or not b.isupper():
#         return 1
#     else:
#         return 0

# Есть точка Р с кор х у есть 2 точка Q x1y1 нати Р1 [0,0] [1,1] [2,2]
# def symmetrick_point (p, q):
#     diff_x = q[0] - p[0]
#     x = q[0] + diff_x
#     diff_y = q[1] - p[1]
#     y = q[0] + diff_y

# print(symmetrick_point(0,0))
