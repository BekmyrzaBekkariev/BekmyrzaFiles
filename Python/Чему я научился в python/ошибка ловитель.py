try:
	print(7 / 0)
except (ZeroDivisionError, NameError, ValueError, TypeError):
	print('Поймана ошибка.')
except:
	print('Поймана ошибка.')

print('Программа завершина !')