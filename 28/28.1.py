def squirrel(N):
    factorial = 1
    for i in range(1, N + 1):
        factorial *= i  # calculating factorial
    first_digit = factorial // 10 ** (len(str(factorial)) - 1)  # dividing factorial
    return first_digit


N = 5
print(squirrel(N))

