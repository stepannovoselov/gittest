import telebot
from token import token

bot = telebot.TeleBot(token)

@bot.message_handler(content_types=["text"])
def message_handler(message):
    pass
def math(first_num, znak, second_num):
    if znak == "+":
        return first_num + second_num
    if znak == '-':
        return first_num - second_num
    if znak == '*':
        return first_num * second_num #
    if znak == '/':
        if second_num == 0:
            return "На ноль делить нельзя"
        else:
            return first_num / second_num
bot.polling(True)