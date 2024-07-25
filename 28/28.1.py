def int_squirrel(int_N):
    factorial = 1
    for i in range(1, int_N + 1):
        factorial *= i  # calculating factorial
    first_digit = factorial // 10 ** (len(str(factorial)) - 1)  # dividing factorial
    return first_digit


int_N = int(input('Vvedite N - '))
print(int_squirrel(int_N))
