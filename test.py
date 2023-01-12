import telebot
from config import token

bot = telebot.TeleBot(token)


def get_math_vaules(example): #
    try:
        num1, znak, num2 = example.split(" ")

        if num1.isnumeric() and num2.isnumeric():
            return [int(num1), znak, int(num2)]
        return []

    except:
        return []


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


@bot.message_handler(content_types=["text"])
def message_handler(message):
    text = message.text

    check = get_math_vaules(text)
    if check != []:
        result = math(*check)
        bot.send_message(message.from_user.id, text=result)


bot.polling(True)
