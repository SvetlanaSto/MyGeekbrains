# Возьмите любые 1-3 задания из прошлых домашних заданий.
# Добавьте к ним логирование ошибок и полезной информации.
# Также реализуйте возможность запуска из командной строки с передачей параметров.


import argparse
import logging

logging.basicConfig(filename="task1.log", level=logging.INFO, encoding='utf-8')
logger = logging.getLogger(__name__)


class TriangleException(Exception):
    pass


class NonExistingTriangleException(TriangleException):
    pass


def check_triangle(a, b, c):
    if a + b <= c or a + c <= b or b + c <= a:
        error_msg = "Треугольника с такими сторонами не существует"
        logger.error(error_msg)
        raise NonExistingTriangleException(error_msg)
    else:
        logger.info("Треугольник существует")

        if a == b == c:
            logger.info("Треугольник равносторонний")
        elif a == b or a == c or b == c:
            logger.info("Треугольник равнобедренный")
        else:
            logger.info("Треугольник разносторонний")


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='checking triangle')
    parser.add_argument('a', metavar='a', type=float, help='enter a')
    parser.add_argument('b', metavar='b', type=float, help='enter b')
    parser.add_argument('c', metavar='c', type=float, help='enter c')
    args = parser.parse_args()
    logger.info(f'В скрипт передано: {args}')

    check_triangle(args.a, args.b, args.c)


