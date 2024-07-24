def squirell(num):
    factorial = 1
    for i in range(1, num + 1):
        factorial *= i  # calculating factorial
    first_digit = factorial // 10 ** (len(str(factorial)) - 1)  # dividing factorial
    return first_digit


try:
    num = int(input('Vvedite N - '))
    if num < 0 or num is float:
        raise ValueError("A number must be positive")
except ValueError as error:
    print("Ошибка:", error)
print(squirell(num))
