import telebot

bot = telebot.TeleBot("1374214931:AAGRqfJoSjKkrfdBxWhOt-P8eADXo7SqhXM")

@bot.message_handler(content_types=['text'])
def send_echo(message):
	bot.reply_to( message, message.text)

bot.polling( none_stop = True)