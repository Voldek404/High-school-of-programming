def degree_recursive(n, m):
    if m < 0:
        return 1 / degree_recursive(n, -m)
    elif m == 0:
        return 1
    elif m == 1:
        return n
    else:
        return n * degree_recursive(n, m - 1)



