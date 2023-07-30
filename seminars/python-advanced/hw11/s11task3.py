# Задание 3
# Добавьте к задачам 1 и 2 строки документации для классов.

from time import time


class Archive:
    """Archive class"""
    __instance = None

    def __init__(self, num: int, text: str):
        self.text = text
        self.num = num

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
            cls.__instance.num_list = []
            cls.__instance.text_list = []
        else:
            cls.__instance.num_list.append(cls.__instance.num)
            cls.__instance.text_list.append(cls.__instance.text)
        return cls.__instance


class MyString(str):
    """MyString class doc"""

    def __new__(cls, value: str, author_name: str):
        instance = super().__new__(cls, value)
        instance.author_name = author_name
        instance.time_created = time()
        print(f'class {cls} created')

        return instance


if __name__ == '__main__':
    # new_arch = Archive(1, 'test')
    # print(help(new_arch))
    print(Archive.__doc__)
    print(MyString.__doc__)
