# Задача 1: Создайте программу для игры в "Крестики-нолики" при помощи виртуального окружения и PIP.
import telebot

bot = telebot.TeleBot('5943898501:AAFgaU1YYA9Jx3km-LGcP4sYoTD2AHgXp9Y')

board = list(range(1, 10))


def draw_board(board, user_id):
    bot.send_message(user_id, f'|{board[0]}|{board[1]}|{board[2]}|\n|{board[3]}|{board[4]}|{board[5]}|\n|{board[6]}|{board[7]}|{board[8]}|')

def make_turn(player_symbol, message):
    player_turn = int(message.text)
    global board
    board[player_turn-1] = player_symbol

@bot.message_handler(commands=['start'])
def start_game(message):
    global board
    board = list(range(1, 10))
    global counter
    counter = 0
    global win
    win = False
    draw_board(board, message.from_user.id)
    bot.send_message(message.from_user.id, "Ход X: ")

@bot.message_handler(content_types=['text'])
def func(message):
    global counter
    if counter % 2 == 0:
        make_turn("X", message)
    else:
        make_turn("O", message)
    draw_board(board, message.from_user.id)
    counter += 1
    if counter > 4:
        tmp = check_win(board)
        if tmp:
            bot.send_message(message.from_user.id, f"{tmp} выиграл!")
            bot.send_message(message.from_user.id, "Начинаем новую игру!")
            start_game(message)
        elif counter % 2 == 0:
            bot.send_message(message.from_user.id, "Ход X: ")
        else:
            bot.send_message(message.from_user.id, "Ход O: ")
    if counter == 9:
        bot.send_message(message.from_user.id, "Ничья!")
        bot.send_message(message.from_user.id, "Начинаем новую игру!")
        start_game(message)

def check_win(board):
    win_coord = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6),
                 (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))
    for each in win_coord:
        if board[each[0]] == board[each[1]] == board[each[2]]:
            return board[each[0]]
    return False

bot.polling(non_stop=True)
