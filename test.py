import telebot
from config import token

bot = telebot.TeleBot(token)


def get_math_vaules(example):
    try:
        num1, znak, num2 = example.split(" ")
        return [num1, znak, num2]

    except:
        return []


@bot.message_handler(content_types=["text"])
def message_handler(message):
    pass


bot.polling(True)
