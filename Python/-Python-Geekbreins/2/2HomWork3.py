# 3. Сформировать из введенного числа обратное по порядку входящих в него цифр и вывести на экран. Например, если введено число 3486, надо вывести 6843.

# Вариант 1
num = int(input('Ведите целое число: '))
result = 0
while num > 0:
    result = result * 10 + num % 10
    num = num // 10
print(result)

# Вариант 2
num = input('Ведите целое число: ')
result = ''
for i in num:
    result = i + result
print(result)

# Вариант 3
# result = num[::-1] - Python Style
num = input('Ведите целое число: ')
result = num[::-1]
print(result)
