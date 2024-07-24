import random

def get_repeated_values(list_of_values, N):
    result = []

    for value in list_of_values:  # сравниваем число повторений с заданным числом N
        if list_of_values.count(value) >= N:
            if value not in result:
                result.append(value)
    return result

list_of_values = [random.randint(1, 10) for _ in range(100)]
N = int(input('Введите число N - '))
print(list_of_values)
repeated_values = get_repeated_values(list_of_values, N)
print(repeated_values)
