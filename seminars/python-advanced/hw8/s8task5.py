# Напишите функцию, которая ищет json файлы в указанной директории и сохраняет их содержимое в виде
# одноимённых pickle файлов.

import os
import json
import pickle


def convert_json_to_pickle(directory):
    for filename in os.listdir(directory):
        if filename.endswith('.json'):
            json_filepath = os.path.join(directory, filename)
            pickle_filepath = os.path.splitext(json_filepath)[0] + '.pickle'

            with open(json_filepath, 'r') as json_file:
                data = json.load(json_file)

            with open(pickle_filepath, 'wb') as pickle_file:
                pickle.dump(data, pickle_file)


if __name__ == '__main__':
    convert_json_to_pickle('.')
