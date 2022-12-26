#  Функция перевода чисел на двоичное число КРУТО

# 1
# def binary(num):
#     s = ''
#     while num > 0:
#         s = f'{num % 2}{s}'
#         num //= 2
#     return s


# print(binary(255))

# Будет спрашивать до тех пор пока не ведет 0
def binary(num):
    s = ''
    while num > 0:
        s = f'{num % 2}{s}'
        num //= 2
    return s


while True:
    n = int(input('Ведите целое число: '))
    if n != 0:
        print(binary(n))
    else:
        break
