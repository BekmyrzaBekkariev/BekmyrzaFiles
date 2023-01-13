text = input('¬ведите текст: ')
lenght = len(text)
kryg = 0
index = 0
while kryg != lenght:
    if index % 2 == 0:
        print(text[index].upper(),end='')
    elif index % 2 == 1:
        print(text[index].lower(),end='')
    else:
        pass
    index += 1
    kryg += 1