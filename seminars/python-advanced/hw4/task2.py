# Напишите функцию принимающую на вход только ключевые параметры и возвращающую словарь,
# где ключ — значение переданного аргумента, а значение — имя аргумента.
# Если ключ не хешируем, используйте его строковое представление.

def process_arguments(**kwargs):
    result = {}
    for key, value in kwargs.items():
        if not isinstance(key, (int, float, str, tuple, frozenset)):
            key = str(key)
        result[value] = key
    return result


if __name__ == '__main__':
    arguments = process_arguments(arg1="value1", arg2="value2", arg3="value3")
    print(arguments)
