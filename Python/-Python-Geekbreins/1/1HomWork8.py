# 8. Вводятся три разных числа. Найти, какое из них является средним (больше одного, но меньше другого).

a = int(input('1 = '))
b = int(input('2 = '))
c = int(input('3 = '))

if b < a < c or c < a < b:
    print('Среднее:', a)
elif a < b < c or c < b < a:
    print('Среднее:', b)
else:
    print('Среднее:', c)
