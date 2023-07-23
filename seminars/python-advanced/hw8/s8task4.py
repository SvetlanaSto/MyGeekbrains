# Прочитайте созданный в прошлом задании csv файл без использования csv.DictReader.
# Дополните id до 10 цифр незначащими нулями.
# В именах первую букву сделайте прописной.
# Добавьте поле хеш на основе имени и идентификатора.
# Получившиеся записи сохраните в json файл, где каждая строка csv файла представлена как отдельный json словарь.
# Имя исходного и конечного файлов передавайте как аргументы функции.


import csv
import json
import hashlib


def process_csv_to_json(input_file, output_file):
    with open(input_file, 'r', newline='') as csv_file, open(output_file, 'w') as json_file:
        reader = csv.reader(csv_file, delimiter='\t')
        next(reader)

        data_list = []
        for row in reader:
            level, id, name = row
            id = id.zfill(10)
            name = name.capitalize()
            hash_value = hashlib.sha256(f'{name}{id}'.encode()).hexdigest()
            data = {
                'level': level,
                'id': id,
                'name': name,
                'hash': hash_value
            }
            data_list.append(data)

        json.dump(data_list, json_file)
        json_file.write('\n')


if __name__ == '__main__':
    process_csv_to_json('my_csv.csv', 's8t4.json')
