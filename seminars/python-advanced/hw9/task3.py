# Напишите функцию:
# Декоратор, запускающий функцию нахождения корней квадратного уравнения с каждой тройкой чисел из csv файла.

import csv


def quadratic_equation_solver(func):
    def wrapper(filename):
        with open(filename, 'r') as csv_file:
            csv_reader = csv.reader(csv_file)
            for row in csv_reader:
                a, b, c = map(float, row)
                func(a, b, c)

    return wrapper


@quadratic_equation_solver
def solve_quadratic_equation(a, b, c):
    discriminant = b ** 2 - 4 * a * c
    if discriminant > 0:
        x1 = (-b + discriminant ** 0.5) / (2 * a)
        x2 = (-b - discriminant ** 0.5) / (2 * a)
        print(f"Для уравнения {a}x^2 + {b}x + {c} корни равны: x1 = {x1}, x2 = {x2}")
    elif discriminant == 0:
        x = -b / (2 * a)
        print(f"Для уравнения {a}x^2 + {b}x + {c} корень равен: x = {x}")
    else:
        print(f"Для уравнения {a}x^2 + {b}x + {c} нет действительных корней")


if __name__ == '__main__':
    solve_quadratic_equation('output.csv')
