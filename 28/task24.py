def MatrixTurn(Matrix, M, N, T):
    rows = len(Matrix)
    cols = len(Matrix[0])
    result = [[0] * cols for _ in range(rows)]
    for i in range(1, cols):
        result[0][i] = Matrix[0][i - 1]
    for i in range(1, rows):
        result[i][cols - 1] = Matrix[i - 1][cols - 1]
    for i in range(cols - 1):
        result[rows - 1][i] = Matrix[rows - 1][i + 1]
    for i in range(rows - 1):
        result[i][0] = Matrix[i + 1][0]
    for i in range(rows):
        for j in range(cols):
            Matrix[i][j] = result[i][j]
