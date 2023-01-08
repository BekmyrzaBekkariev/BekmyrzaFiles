import random

num = random.randint(0, 100)
print("Отгадать число от 0 до 100 за 10 попыток")
for i in range(1, 11):
    answer = int(input(f'Попытка {i}: '))
    if num < answer:
        print("Число меньше")
    elif num > answer:
        print("Число больше")
    else:
        print(f"Вы угадали с {i}-й попытки")
        break
else:
    print(f" Поражение. Было загадано {num}")
