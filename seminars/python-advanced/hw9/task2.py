# Напишите функцию:
# Генерация csv файла с тремя случайными числами в каждой строке. 100-1000 строк.

import csv
import random


def generate_csv(filename):
    with open(filename, 'w', newline='') as csv_file:
        csv_writer = csv.writer(csv_file)
        num_rows = random.randint(100, 1000)
        for _ in range(num_rows):
            row = [random.randint(1, 1000) for _ in range(3)]
            csv_writer.writerow(row)


if __name__ == '__main__':
    generate_csv('output.csv')


