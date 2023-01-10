
# Циклы, Рекурсии, Функции

# 2.1
# Цикл с предусловием
num = int(input('Ведите целое число'))
while num > 0:
    print(num % 10)
    num //= 10

# Цикл с постусловием
while True:
    num = float(input('Ведите чила от 0 до 100: '))
    if num >= 0 and num <= 100:
        break
print('Этот вывод вне цикла.')

# Цикл с параметром while
i = 0
while i <= 10:
    print(i)
    i += 1

for i in range(11):
    print(i)
# мой пример
for i in range(int(input('Ведите до скольки'))):
    print(i + 1)
