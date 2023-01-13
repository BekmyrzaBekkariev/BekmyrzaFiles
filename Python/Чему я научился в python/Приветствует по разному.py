name = input("Ваше имя: ")

if (name.lower().startswith("а") or name.lower().startswith("a") ):
	print('Добро пожаловать \nВы находитесь в элитном клубе людей!')
else:
	print("Добро пожаловать игрок!")