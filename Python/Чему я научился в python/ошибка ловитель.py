try:
	print(7 / 0)
except (ZeroDivisionError, NameError, ValueError, TypeError):
	print('������� ������.')
except:
	print('������� ������.')

print('��������� ��������� !')