dog = input('Какое слово заполнить?')
length = 10

if (len(dog) % 2 ):
	length += 1 

print( ('{0:*^' + str(length)+'}').format( dog )) 