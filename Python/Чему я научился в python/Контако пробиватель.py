contacts = {
	"�������� ��������� " :"+6565656",
	"������ ���������" : "+82054065"
}

test = input('���� ����?  :')
if test in contacts:
	print("������ ������ : " + contacts[test] )
else:
	print("������ �� ������! ")