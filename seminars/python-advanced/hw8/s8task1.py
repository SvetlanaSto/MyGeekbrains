# Вспоминаем задачу 3 из прошлого семинара. Мы сформировали текстовый файл с псевдоименами и произведением чисел.
# Напишите функцию, которая создаёт из созданного ранее файла новый с данными в формате JSON.
# Имена пишите с большой буквы.
# Каждую пару сохраняйте с новой строки.

import json


def file_to_json(path: str) -> None:
    my_dict = {}
    with open(path, 'r', encoding='utf-8') as f:
        for line in f:
            name, number = line[:-2].split(' ')
            my_dict[name.capitalize()] = float(number)
    print(my_dict)
    with open('my_json.json', 'w', encoding='utf-8') as j:
        json.dump(my_dict, j, ensure_ascii=False, indent=2)


if __name__ == '__main__':
    file_to_json('t3.txt')
