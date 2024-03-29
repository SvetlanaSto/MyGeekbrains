# Напишите функцию для транспонирования матрицы

def transpose_matrix(matrix):
    rows = len(matrix)
    cols = len(matrix[0])

    transposed = [[0 for _ in range(rows)] for _ in range(cols)]

    for i in range(rows):
        for j in range(cols):
            transposed[j][i] = matrix[i][j]

    return transposed


if __name__ == '__main__':
    matrix = [[1, 2, 3],
              [4, 5, 6]]

    result = transpose_matrix(matrix)
    print(result)
