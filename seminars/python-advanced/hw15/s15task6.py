# Напишите код, который запускается из командной строки и получает на вход путь до директории на ПК.
# Соберите информацию о содержимом в виде объектов namedtuple.
# Каждый объект хранит:
# имя файла без расширения или название каталога,
# расширение, если это файл,
# флаг каталога,
# название родительского каталога.
# В процессе сбора сохраните данные в текстовый файл используя логирование.

import os
import argparse
import logging
from collections import namedtuple

logging.basicConfig(filename="log6.log", level=logging.INFO, encoding='utf-8')
logger = logging.getLogger(__name__)

file = namedtuple(typename='file', field_names='file_name, ext, folder, parent_folder')


def directory_info(file_p: str):
    files_list = os.listdir(file_p)
    p = file_p.split(os.path.sep)
    for item in files_list:
        if os.path.isfile(f'{os.path.sep}'.join([file_p, item])):
            temp = item.split('.')
            obj = file(temp[0], temp[1], p[-1], f'{os.path.sep}'.join(p[:-1]))
        else:
            obj = file(item, '', p[-1], f'{os.path.sep}'.join(p[:-1]))
        logger.info(obj)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='parser')
    parser.add_argument('path',
                        metavar='file_p',
                        type=str,
                        nargs='?', help='enter dir path')
    args = parser.parse_args()
    print(f'В скрипт передано: {args}')
    print(directory_info(args.path))

