import mult
import sum
import div
import sub
import logger

import telebot

bot = telebot.TeleBot('5943898501:AAFgaU1YYA9Jx3km-LGcP4sYoTD2AHgXp9Y')


@bot.message_handler(commands=['start', 'help'])
def menu(message):
    bot.send_message(message.from_user.id, 'Введите номер операции и два числа (например, 1 3 2 для операции "3 * 2"): \n1: умножение\n2: деление\n3: сложение\n4: вычитание')


@bot.message_handler(content_types=['text'])
def operation(message):
    try:
        command = message.text.split()
        op = int(command[0])
        a = int(command[1])
        b = int(command[2])
        if op == 1:
            result = mult.mult_numbers(a, b)
            logger.mult_logger(a, b, result)
            bot.send_message(message.from_user.id, result)
        if op == 2:
            result = div.Div(a, b)
            logger.div_logger(a, b, result)
            bot.send_message(message.from_user.id, result)
        if op == 3:
            result = sum.Sum(a, b)
            logger.sum_logger(a, b, result)
            bot.send_message(message.from_user.id, result)
        if op == 4:
            result = sub.sub(a, b)
            logger.sub_logger(a, b, result)
            bot.send_message(message.from_user.id, result)
    except:
        bot.send_message(message.from_user.id, "Ошибка! Введите операцию в правильном формате:")
        menu(message)


bot.polling(non_stop=True)
