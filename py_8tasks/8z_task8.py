def army_communication_matrix(n: int, matrix: list):
    prefix_sum = [[0] * n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            prefix_sum[i][j] = matrix[i][j]
            if i > 0:
                prefix_sum[i][j] += prefix_sum[i - 1][j]
            if j > 0:
                prefix_sum[i][j] += prefix_sum[i][j - 1]
            if i > 0 and j > 0:
                prefix_sum[i][j] -= prefix_sum[i - 1][j - 1]

    max_sum = 0
    bestX, bestY, bestM = 0, 0, 0

    for m in range(2, n):
        for i in range(n - m + 1):
            for j in range(n - m + 1):
                x1, y1 = i, j
                x2, y2 = i + m - 1, j + m - 1
                current_sum = prefix_sum[x2][y2]
                if x1 > 0:
                    current_sum -= prefix_sum[x1 - 1][y2]
                if y1 > 0:
                    current_sum -= prefix_sum[x2][y1 - 1]
                if x1 > 0 and y1 > 0:
                    current_sum += prefix_sum[x1 - 1][y1 - 1]

                if current_sum > max_sum:
                    max_sum = current_sum
                    bestX, bestY, bestM = x1, y1, m

    return f"{bestX} {bestY} {bestM}"



