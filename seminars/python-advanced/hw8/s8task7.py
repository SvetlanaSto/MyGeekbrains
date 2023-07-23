# Прочитайте созданный в прошлом задании csv файл без использования csv.DictReader.
# Распечатайте его как pickle строку.


import csv
import pickle


def process_csv_to_pickle(csv_file):
    with open(csv_file, 'r', newline='') as f:
        reader = csv.reader(f, delimiter=',')
        next(reader)

        data_list = []
        for row in reader:
            data_list.append(row)

        res = pickle.dumps(data_list, protocol=pickle.DEFAULT_PROTOCOL)
        print(f'{res = }')


if __name__ == '__main__':
    process_csv_to_pickle('s8t6.csv')
