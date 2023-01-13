# Дебилный калькулятор  V2

from colorama import init
from colorama import Fore, Back, Style

# use Colorama to make Termcolor work on Windows too
init()

print(Back.GREEN)
print(Fore.BLACK)

what = input("Что делаем? (+, -, /, *)" )

print(Back.BLUE)
print(Fore.BLACK)

a = float( input("Ведите первое число:") )
b = float( input("Ведите второе число:") )

print(Back.RED)
print(Fore.BLACK)

if what == "+":
    c = a + b
    print("Результат:" + str(c))
elif what == "-":
    c = a - b
    print("Результат:" + str(c))
elif what == "*":
    c = a * b
    print("Результат:" + str(c))
elif what == "/":
    c = a / b
    print("Результат:" + str(c))
else:
	print("Выброна не верное операция!")