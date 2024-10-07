import random


def get_repeated_values(list_of_values, min_repeat):
    count_dict = {}

    for value in list_of_values:  # считаем количество повторений
        if value not in count_dict:
            count_dict[value] = 0
        count_dict[value] += 1

    result = []
    for key, value in count_dict.items():  # сравниваем число повторений с заданным числом N
        if value == min_repeat:
            result.append(key)
    return result


list_of_values = [random.randint(1, 10) for _ in range(100)]
N = int(input('Введите число N - '))
print(list_of_values)
repeated_values = get_repeated_values(list_of_values, N)
print(repeated_values)
