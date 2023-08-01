# Возьмите 1-3 задачи из тех, что были на прошлых семинарах или в домашних заданиях.
# Напишите к ним классы исключения с выводом подробной информации. Поднимайте исключения внутри основного кода.
# Например нельзя создавать прямоугольник со сторонами отрицательной длины.
class TriangleException(Exception):
    pass


class EdgeSizeIsNonPositiveException(TriangleException):
    pass


class NonExistingTriangleException(TriangleException):
    pass


def validate_edge_size(size: float):
    if size <= 0:
        raise EdgeSizeIsNonPositiveException


def get_edge_size(edge_name: str):
    while True:
        try:
            result = float(input(f"Введите длину стороны треугольника {edge_name}: "))
            validate_edge_size(result)
            return result
        except EdgeSizeIsNonPositiveException:
            print('Длина стороны треугольника должна быть больше нуля!')
        except ValueError:
            print('введите длину в числовом формате')


def check_triangle(a, b, c):
    if a + b <= c or a + c <= b or b + c <= a:
        raise NonExistingTriangleException("Треугольника с такими сторонами не существует")
    else:
        print("Треугольник существует")

        if a == b == c:
            print("Треугольник равносторонний")
        elif a == b or a == c or b == c:
            print("Треугольник равнобедренный")
        else:
            print("Треугольник разносторонний")


if __name__ == '__main__':
    a = get_edge_size('A')
    b = get_edge_size('B')
    c = get_edge_size('C')
    check_triangle(a, b, c)
