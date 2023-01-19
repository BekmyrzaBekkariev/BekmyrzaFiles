# Уравнение  == сколько вариантов уровнения к цифре

p, q = map(int, input().split())
c = 0
for x in range(1, q):
    for y in range(1, q):
        if x * y + p * x == q:
            c += 1
            print(x, y)
print(c)
