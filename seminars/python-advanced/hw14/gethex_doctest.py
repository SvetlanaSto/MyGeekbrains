def test_get_hex(n):
    """
    Функция переводит число в шестнадцатеричную систему счисления.

    Параметры:
    - n: целое число

    Возвращает:
    - Шестнадцатеричное представление числа

    Импорт модуля:
    >>> from hw14.gethex import get_hex

    Примеры использования:
    >>> get_hex(10)
    'a'
    >>> get_hex(16)
    '10'
    >>> get_hex(255)
    'ff'
    >>> get_hex(1024)
    '400'
    >>> get_hex(0)
    '0'
    >>> get_hex('hello')
    Traceback (most recent call last):
    ...
    TypeError: not all arguments converted during string formatting
    """


if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)

