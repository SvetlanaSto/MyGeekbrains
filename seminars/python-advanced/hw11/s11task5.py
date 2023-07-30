# Задание 5
# Дорабатываем класс прямоугольник из прошлого семинара.
# Добавьте возможность сложения и вычитания.
# При этом должен создаваться новый экземпляр прямоугольника.
# Складываем и вычитаем периметры, а не длинну и ширину.
# При вычитании не допускайте отрицательных значений.
# Добавьте ко всем задачам с семинара строки документации и методы вывода информации на печать.

class Rectangle:
    """Rectangle class"""

    def __init__(self, width: float, height: float = None):
        self.width = width
        if height is None:
            self.height = width
        else:
            self.height = height

    def calc_perimeter(self):
        """Calculate perimeter"""

        return (self.width + self.height) * 2

    def calc_area(self):
        """Calculate area"""

        return self.width * self.height
    
    def __add__(self, other):
        perimeter = self.calc_perimeter() + other.calc_perimeter()
        width = self.width + other.width
        height = perimeter / 2 - width
        return Rectangle(width, height)

    def __sub__(self, other):
        if self.calc_perimeter() < other.calc_perimeter():
            self, other = other, self
        width = abs(self.width - other.width)
        perimeter = self.calc_perimeter() - other.calc_perimeter()
        height = perimeter / 2 - width
        return Rectangle(width, height)

    def __str__(self):
        return f'perimeter = {self.calc_perimeter()}, width = {self.width}, height = {self.height}'


if __name__ == '__main__':
    new_rect = Rectangle(10, 20)
    new_square = Rectangle(10)

    print(new_rect + new_square)
    print(new_rect - new_square)

    print(Rectangle.__doc__)
    print(new_rect.calc_perimeter.__doc__)
    print(new_rect.calc_area.__doc__)
