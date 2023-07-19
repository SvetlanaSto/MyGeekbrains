# Создайте функцию для сортировки файлов по директориям: видео, изображения, текст и т.п.
# Каждая группа включает файлы с несколькими расширениями.
# В исходной папке должны остаться только те файлы, которые не подошли для сортировки.

import os
import shutil


def move_files_by_type(files_dir):
    file_types = {
        'Изображения': ['.jpg', '.jpeg', '.png', '.gif'],
        'Видео': ['.mp4', '.avi', '.mov', '.mkv'],
        'Текст': ['.txt', '.doc', '.docx', '.pdf'],
    }

    for filename in os.listdir(files_dir):
        if os.path.isfile(os.path.join(files_dir, filename)):
            file_extension = os.path.splitext(filename)[1]

            for file_group, extensions in file_types.items():
                if file_extension.lower() in extensions:
                    group_dir = os.path.join(files_dir, file_group)
                    os.makedirs(group_dir, exist_ok=True)
                    shutil.move(os.path.join(files_dir, filename), os.path.join(group_dir, filename))
                    break
            else:
                shutil.move(os.path.join(files_dir, filename), os.path.join(files_dir, filename))


if __name__ == '__main__':
    move_files_by_type('files')
