# Напишите функцию:
# Декоратор, сохраняющий переданные параметры и результаты работы функции в json файл.

import json


def save_to_json(filename):
    def decorator(func):
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            data = {
                "params": {
                    "args": args,
                    "kwargs": kwargs
                },
                "result": result
            }
            with open(filename, 'w') as json_file:
                json.dump(data, json_file, indent=4)
            return result

        return wrapper

    return decorator


@save_to_json('output.json')
def example_function(a, b):
    result = a + b
    return result


if __name__ == '__main__':
    example_function(3, 4)
