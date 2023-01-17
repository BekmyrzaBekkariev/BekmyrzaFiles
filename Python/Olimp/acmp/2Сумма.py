
# Требуется посчитать сумму целых чисел, расположенных между числами 1 и N включительно

# 1
N = int(input())
sum = 0
for i in range(N + 1):
    sum += i
print(sum)

# 2
N = int(input())
sum = (N * (N + 1)) // 2
print(sum)

# 3
N = int(input())
print((N*(N+1))//2)
