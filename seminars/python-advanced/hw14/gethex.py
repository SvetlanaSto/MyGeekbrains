def get_hex(num):
    hexadecimal = ''
    hex_chars = '0123456789abcdef'

    if num == 0:
        return '0'

    while num != 0:
        remainder = num % 16
        hexadecimal = hex_chars[remainder] + hexadecimal
        num = num // 16

    return hexadecimal


if __name__ == '__main__':
    dec = int(input("Введите целое число: "))
    result = get_hex(dec)
    print(f"Шестнадцатеричное представление числа {dec}:", result)

    expected = hex(dec)
    print("Проверка через функцию hex:", expected)

