import print1
import sort

import telebot
bot = telebot.TeleBot('5943898501:AAFgaU1YYA9Jx3km-LGcP4sYoTD2AHgXp9Y')

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.from_user.id, "База данных сотрудников.")
    bot.send_message(message.from_user.id, '1. Вывести все записи.\n2. Экспорт CSV с сортировкой по фамилии.\n3. Экспорт CSV с сортировкой id.')

@bot.message_handler(content_types=['text'])
def menu(message):
    value = int(message.text)

    if value == 1:
        result = print1.print_all_to_bot()
        bot.send_message(message.from_user.id, result)
    elif value == 2:
        result = sort.sort_by_lastname('employees.csv')
        bot.send_message(message.from_user.id, result)
    elif value == 3:
        result = sort.sort_by_id('employees.csv')
        bot.send_message(message.from_user.id, result)
    else:
        bot.send_message(message.from_user.id, "Укажите корректный пункт меню.")

bot.polling(non_stop=True)