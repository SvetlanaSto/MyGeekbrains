# Задача 3: Создайте программу для игры в "Крестики-нолики".

board = list(range(1, 10))


def draw_board(board):
    for i in range(3):
        print("|", board[0+i*3], "|", board[1+i*3], "|", board[2+i*3], "|")


def make_turn(player_symbol):
    player_turn = int(input("Ход " + player_symbol + ": "))
    board[player_turn-1] = player_symbol


def check_win(board):
    win_coord = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6),
                 (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))
    for each in win_coord:
        if board[each[0]] == board[each[1]] == board[each[2]]:
            return board[each[0]]
    return False


counter = 0
win = False
while not win:
    draw_board(board)
    if counter % 2 == 0:
        make_turn("X")
    else:
        make_turn("O")
    counter += 1
    if counter > 4:
        tmp = check_win(board)
        if tmp:
            print(tmp, "выиграл!")
            win = True
            break
    if counter == 9:
        print("Ничья!")
        break
draw_board(board)
