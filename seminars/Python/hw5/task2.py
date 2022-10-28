# Задача 2: Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. Все конфеты оппонента достаются сделавшему последний ход. Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
# a) Добавьте игру против бота
# b) Подумайте как наделить бота "интеллектом"

import random

candies = 2021


def bot_turn():
    amount = candies % 29
    print('Бот забрал конфет:', amount)
    return amount


def player_turn():
    amount = int(
        input(f'Текущее число конфет: {candies}. Возьмите от 1 до 28 конфет: '))
    return amount


if (random.randint(1, 2) == 1):
    amount = bot_turn()
    candies -= amount

while candies > 0:
    amount = player_turn()
    candies -= amount
    if candies == 0:
        print('Вы победили!')
        exit()
    amount = bot_turn()
    candies -= amount
    if candies == 0:
        print('Бот победил. Game over.')
