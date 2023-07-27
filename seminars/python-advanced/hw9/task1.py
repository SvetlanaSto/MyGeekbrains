# Напишите функцию: Нахождение корней квадратного уравнения

import math


def quadratic_equation_solver(func):
    def wrapper(a, b, c):
        discriminant = b ** 2 - 4 * a * c

        if discriminant >= 0:
            x1 = (-b + math.sqrt(discriminant)) / (2 * a)
            x2 = (-b - math.sqrt(discriminant)) / (2 * a)
            return func(a, b, c, x1, x2)
        else:
            return "Нет действительных корней"

    return wrapper


@quadratic_equation_solver
def solve_quadratic_equation(a, b, c, x1, x2):
    print(f"Корни квадратного уравнения {a}x^2 + {b}x + {c} равны: x1 = {x1}, x2 = {x2}")


if __name__ == '__main__':
    solve_quadratic_equation(1, -3, 2)
