# Напишите функцию, которая генерирует псевдоимена.
# Имя должно начинаться с заглавной буквы, состоять из 4-7 букв, среди которых обязательно должны быть гласные.
# Полученные имена сохраните в файл.

from random import choice, randint

LETTER_VOVS = 'aeiouy'
LETTER_CONS = 'dcdfghjklmnprstvwxz'
NAME_LENGHT_MIN = 4
NAME_LENGHT_MAX = 7


def psevdo_gen(num_names: int, file_name: str) -> None:
    with open(file_name, 'a', encoding='utf-8') as f:
        for _ in range(num_names):
            name = ''.join(choice(LETTER_VOVS) if i in (1, 4, 6) else choice(LETTER_CONS)
                           for i in range(randint(NAME_LENGHT_MIN, NAME_LENGHT_MAX)))
        f.write(name.capitalize() + '\n')


if __name__ == '__main__':
    psevdo_gen(10, 't2.txt')
