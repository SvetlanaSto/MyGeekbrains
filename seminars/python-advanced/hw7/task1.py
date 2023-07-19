# Напишите функцию группового переименования файлов. Она должна:
# принимать параметр желаемое конечное имя файлов. При переименовании в конце имени добавляется порядковый номер.
# принимать параметр количество цифр в порядковом номере.
# принимать параметр расширение исходного файла. Переименование должно работать только для этих файлов внутри каталога.
# принимать параметр расширение конечного файла.
# принимать диапазон сохраняемого оригинального имени. Например для диапазона [3, 6] берутся буквы с 3 по 6 из исходного
# имени файла. К ним прибавляется желаемое конечное имя, если оно передано. Далее счётчик файлов и расширение.

import os


def batch_rename_files(directory, final_name, num_digits, source_extension, final_extension, start_char=3, end_char=6):
    counter = 1
    for filename in os.listdir(directory):
        if filename.endswith(source_extension):
            original_name = filename[start_char:end_char]
            new_name = original_name + final_name + str(counter).zfill(num_digits) + final_extension
            os.rename(os.path.join(directory, filename), os.path.join(directory, new_name))
            counter += 1


if __name__ == '__main__':
    directory = 'files'
    final_name = '_new'
    num_digits = 3
    source_extension = '.txt'
    final_extension = '.pdf'
    start_char = 3
    end_char = 6

    batch_rename_files(directory, final_name, num_digits, source_extension, final_extension, start_char, end_char)
