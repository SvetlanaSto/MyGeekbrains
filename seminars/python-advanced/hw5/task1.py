# Напишите функцию, которая принимает на вход строку — абсолютный путь до файла.
# Функция возвращает кортеж из трёх элементов: путь, имя файла, расширение файла.

import os

def parse_file_path(file_path):
    path, file_name = os.path.split(file_path)
    file_name, file_extension = os.path.splitext(file_name)
    return path, file_name, file_extension

file_path = '/home/sveta/geekbrains 2/Тестирование API/дз 2/icon-1366.png'
result = parse_file_path(file_path)
print(result)
