import mult
import sum
import div
import sub
import logger

import telebot

bot = telebot.TeleBot('5943898501:AAFgaU1YYA9Jx3km-LGcP4sYoTD2AHgXp9Y')


@bot.message_handler(commands=['start', 'help'])
def menu(message):
    bot.send_message(message.from_user.id, 'Введите номер операции и два числа (например, 3 * 2 для операции "3 * 2"): \n1: умножение\n2: деление\n3: сложение\n4: вычитание\n\n/logs - история вычислений')

@bot.message_handler(commands=['logs'])
def get_logs(message):
    bot.send_message(message.from_user.id, logger.get_logs())


@bot.message_handler(content_types=['text'])
def operation(message):
    try:
        command = message.text.split()
        op = command[1]
        a = int(command[0])
        b = int(command[2])
        if op == "*":
            result = mult.mult_numbers(a, b)
            logger.mult_logger(a, b, result)
            bot.send_message(message.from_user.id, result)
        if op == "/":
            result = div.Div(a, b)
            logger.div_logger(a, b, result)
            bot.send_message(message.from_user.id, result)
        if op == "+":
            result = sum.Sum(a, b)
            logger.sum_logger(a, b, result)
            bot.send_message(message.from_user.id, result)
        if op == "-":
            result = sub.sub(a, b)
            logger.sub_logger(a, b, result)
            bot.send_message(message.from_user.id, result)
        else:
            bot.send_message(message.from_user.id, f"Ошибка! Операция {op} не поддерживается")
            menu(message)
    except:
        bot.send_message(message.from_user.id, "Ошибка! Введите операцию в правильном формате:")
        menu(message)


bot.polling(non_stop=True)
