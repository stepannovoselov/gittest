import telebot
from token import token

bot = telebot.TeleBot(token)

@bot.message_handler(content_types=["text"])
def message_handler(message):
    pass

bot.polling(True)