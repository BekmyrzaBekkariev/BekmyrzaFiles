contacts = {
	"Бекмырза Беккариев " :"+6565656",
	"Алихан Беккариев" : "+82054065"
}

test = input('Кого ищем?  :')
if test in contacts:
	print("Контак найден : " + contacts[test] )
else:
	print("Контак не найден! ")