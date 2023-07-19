# Дорабатываем функции из предыдущих задач.
# Генерируйте файлы в указанную директорию — отдельный параметр функции.
# Отсутствие/наличие директории не должно вызывать ошибок в работе функции (добавьте проверки).
# Существующие файлы не должны удаляться/изменяться в случае совпадения имён.

from random import choices, randint
from string import ascii_lowercase, digits
import os


def gen_ext(ext: str, name_len_min: int = 6, name_len_max: int = 30, bytes_min: int = 256, bytes_max: int = 4096,
            num_files: int = 3, dir: str = '.') -> None:
    os.makedirs(dir, exist_ok=True)
    for _ in range(num_files):
        name = ''.join(choices(ascii_lowercase + digits + '_', k=randint(name_len_min, name_len_max)))
        data = bytes(randint(0, 255) for _ in range(randint(bytes_min, bytes_max)))
        with open(f'{dir}/{name}.{ext}', 'wb') as f:
            f.write(data)


if __name__ == '__main__':
    gen_ext('txt', dir='files')


