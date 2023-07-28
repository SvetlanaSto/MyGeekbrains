# Возьмите 1-3 любые задания из прошлых семинаров (например сериализация данных), которые вы уже решали.
# Превратите функции в методы класса, а параметры в свойства. Задания должны решаться через вызов методов экземпляра.

class Tree:

    def __init__(self, length: int):
        self.length = length

    def draw(self):
        for i in range(1, self.length + 1):
            spaces = ' ' * (self.length - i)
            stars = '*' * (2 * i - 1)
            print(spaces + stars)


class Matrix:

    def __init__(self, matrix):
        self.matrix = matrix

    def transpose(self):
        rows = len(self.matrix)
        cols = len(self.matrix[0])

        transposed = [[0 for _ in range(rows)] for _ in range(cols)]

        for i in range(rows):
            for j in range(cols):
                transposed[j][i] = self.matrix[i][j]

        return transposed


class Calculator:

    def get_hex(self, num):
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
    tree = Tree(5)
    tree.draw()
    print()

    m = Matrix([[1, 2, 3], [4, 5, 6]])
    transposed = m.transpose()
    print(transposed)
    print()

    calc = Calculator()
    dec = 30
    hex_ = calc.get_hex(dec)
    print(f"Шестнадцатеричное представление числа {dec}:", hex_)
