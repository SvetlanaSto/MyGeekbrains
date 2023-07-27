# Создайте функцию-замыкание, которая запрашивает два целых числа:
# от 1 до 100 для загадывания,
# от 1 до 10 для количества попыток
# Функция возвращает функцию, которая через консоль просит угадать загаданное число за указанное число попыток.

from typing import Callable


def gess_number(number: int, count: int) -> Callable[[], None]:
    def gess():
        for i in range(1, count + 1):
            print(f'Попытка № {count}')
            num_input = int(input('Введите число: '))
            if num_input == number:
                print('Вы угадали!')
                break
            elif num_input < number:
                print('Ваше число меньше')
            else:
                print('Ваше число больше')

    return gess


if __name__ == '__main__':
    game = gess_number(25, 5)
    game()

