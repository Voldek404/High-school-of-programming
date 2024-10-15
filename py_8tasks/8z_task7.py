def rotate_matrix_recursive(matrix_copy):
    if len(matrix_copy) == 0:
        return []

    def rotate_helper(i):
        if i < 0:
            return []
        return [[row[i] for row in matrix_copy]] + rotate_helper(i - 1)

    return rotate_helper(len(matrix_copy[0]) - 1)


def snake_array(matrix_copy, new_matrix):
    if not matrix_copy:
        return new_matrix
    new_matrix += matrix_copy[0]
    matrix_copy = matrix_copy[1:]
    if matrix_copy:
        matrix_copy = rotate_matrix_recursive(matrix_copy)
    return snake_array(matrix_copy, new_matrix)


matrix = [[1, 2, 3, 4, 5, 6], [7, 8, 9, 10, 11, 12], [13, 14, 15, 16, 17, 18]]
matrix_copy = matrix.copy()
new_matrix = []
print(snake_array(matrix_copy, new_matrix))
