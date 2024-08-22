def sum_of_digits_recursive(number):
    if number == 0:
        return 0
    else:
        return number % 10 + sum_of_digits_recursive(number // 10)



