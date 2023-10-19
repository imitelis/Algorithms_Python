# Matrixes

def matrix_addition(matrix1, matrix2):
    result = []
    for i in range(len(matrix1)):
        row = []
        for j in range(len(matrix1[0])):
            row.append(matrix1[i][j] + matrix2[i][j])
        result.append(row)
    return result

# Example usage
matrix1 = [[1, 2], [3, 4]]
matrix2 = [[5, 6], [7, 8]]
result = matrix_addition(matrix1, matrix2)
print(result)  # Output: [[6, 8], [10, 12]]


def matrix_subtraction(matrix1, matrix2):
    result = []
    for i in range(len(matrix1)):
        row = []
        for j in range(len(matrix1[0])):
            row.append(matrix1[i][j] - matrix2[i][j])
        result.append(row)
    return result

# Example usage
matrix1 = [[1, 2], [3, 4]]
matrix2 = [[5, 6], [7, 8]]
result = matrix_subtraction(matrix1, matrix2)
print(result)  # Output: [[-4, -4], [-4, -4]]


def matrix_multiplication(matrix1, matrix2):
    result = [[0 for _ in range(len(matrix2[0]))] for _ in range(len(matrix1))]
    for i in range(len(matrix1)):
        for j in range(len(matrix2[0])):
            for k in range(len(matrix2)):
                result[i][j] += matrix1[i][k] * matrix2[k][j]
    return result

# Example usage
matrix1 = [[1, 2], [3, 4]]
matrix2 = [[5, 6], [7, 8]]
result = matrix_multiplication(matrix1, matrix2)
print(result)  # Output: [[19, 22], [43, 50]]


def transpose_matrix(matrix):
    return [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]

# Example usage
matrix = [[1, 2, 3], [4, 5, 6]]
transposed_matrix = transpose_matrix(matrix)
print(transposed_matrix)  # Output: [[1, 4], [2, 5], [3, 6]]