# Напишите функцию, которая получает на вход директорию и рекурсивно обходит её и все вложенные директории.
# Результаты обхода сохраните в файлы json, csv и pickle.
# Для дочерних объектов указывайте родительскую директорию.
# Для каждого объекта укажите файл это или директория.
# Для файлов сохраните его размер в байтах, а для директорий размер файлов в ней с учётом всех вложенных файлов и директорий.

import os
import json
import csv
import pickle


def save_directory_info(directory):
    file_info = []

    for path, dirs, files in os.walk(directory):
        dir_size = sum(os.path.getsize(os.path.join(path, file)) for file in files)
        dir_info = {"path": path, "type": "directory", "size": dir_size}
        file_info.append(dir_info)

        for file in files:
            file_path = os.path.join(path, file)
            file_size = os.path.getsize(file_path)
            file_info.append({"path": file_path, "type": "file", "size": file_size})

    json_file = "directory_info.json"
    csv_file = "directory_info.csv"
    pickle_file = "directory_info.pickle"

    with open(json_file, "w") as f:
        json.dump(file_info, f, indent=4)

    with open(csv_file, "w", newline='') as f:
        writer = csv.DictWriter(f, fieldnames=["path", "type", "size"])
        writer.writeheader()
        writer.writerows(file_info)

        with open(pickle_file, "wb") as f:
            pickle.dump(file_info, f)


if __name__ == '__main__':
    directory_path = "/home/sveta/УЧЕБА/MyGeekbrains/seminars/python-advanced/"
    save_directory_info(directory_path)
