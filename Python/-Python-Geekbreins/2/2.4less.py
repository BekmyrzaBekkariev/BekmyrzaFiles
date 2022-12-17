# НОД ВАРИАНТ 1
# ПРОСТЕЙШИЙ ЦИКЛИЧЕСКИЙ АЛГОРИТМ

def gcd(m, n):
    while m != n:
        if m > n:
            m -= n
        else:
            n -= m
    return m


print(gcd(54, 24))


# НОД ВАРИАНТ 2
# РЕКУРСИВНЫЙ АЛГОРИТМ

def gcd2(m, n):
    if n == 0:
        return m
    return gcd2(n, m % n)


print(gcd2(54, 24))


# НОД ВАРИАНТ 3
# ЦЫКЛИЧЕСКИЙ АЛГОРИТМ

def gcd3(m, n):
    while n != 0:
        m, n = n, m % n
    return m


print(gcd2(54, 24))
