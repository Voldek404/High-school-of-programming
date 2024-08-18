def get_layer(Matrix, layer):
    rows, cols = len(Matrix), len(Matrix[0])
    top_row = layer
    bottom_row = rows - layer - 1
    left_col = layer
    right_col = cols - layer - 1

    layer_elements = []

    for col in range(left_col, right_col + 1):
        layer_elements.append(Matrix[top_row][col])

    for row in range(top_row + 1, bottom_row + 1):
        layer_elements.append(Matrix[row][right_col])

    for col in range(right_col - 1, left_col - 1, -1):
        layer_elements.append(Matrix[bottom_row][col])

    for row in range(bottom_row - 1, top_row, -1):
        layer_elements.append(Matrix[row][left_col])


    layer_elements = layer_elements[-1:] + layer_elements[:-1]


    index = 0

    for col in range(left_col, right_col + 1):
        Matrix[top_row][col] = layer_elements[index]
        index += 1

    for row in range(top_row + 1, bottom_row + 1):
        Matrix[row][right_col] = layer_elements[index]
        index += 1

    for col in range(right_col - 1, left_col - 1, -1):
        Matrix[bottom_row][col] = layer_elements[index]
        index += 1

    for row in range(bottom_row - 1, top_row, -1):
        Matrix[row][left_col] = layer_elements[index]
        index += 1

def MatrixTurn(Matrix, M, N, T):

    Matrix = [list(row) for row in Matrix]


    num_layers = min(M, N) // 2

    for _ in range(T):
        for layer in range(num_layers):
            get_layer(Matrix, layer)

    for i in range(M):
        Matrix[i] = ''.join(Matrix[i])


