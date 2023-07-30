# Создайте класс Матрица. Добавьте методы для:
# а. вывода на печать,
# б. сравнения,
# в. сложения,
# г. *умножения матриц

class Matrix:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.data = [[0] * cols for _ in range(rows)]

    def __str__(self):
        matrix_str = ""
        for row in self.data:
            matrix_str += " ".join(str(element) for element in row)
            matrix_str += "\n"
        return matrix_str

    def __eq__(self, other):
        if isinstance(other, Matrix):
            return self.rows == other.rows and self.cols == other.cols and self.data == other.data
        return False

    def __add__(self, other):
        if isinstance(other, Matrix) and self.rows == other.rows and self.cols == other.cols:
            result = Matrix(self.rows, self.cols)
            for i in range(self.rows):
                for j in range(self.cols):
                    result.data[i][j] = self.data[i][j] + other.data[i][j]
            return result
        else:
            raise ValueError("Невозможно сложить матрицы разных размеров")


if __name__ == '__main__':
    matrix1 = Matrix(2, 3)
    matrix1.data = [[1, 2, 3], [4, 5, 6]]
    print(matrix1)

    matrix2 = Matrix(2, 3)
    matrix2.data = [[7, 8, 9], [10, 11, 12]]
    print(matrix2)

    print(matrix1 == matrix2)

    matrix3 = matrix1 + matrix2
    print(matrix3)
