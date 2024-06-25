import random
import requests


def get_list_of_words(path):  # считываем дефолтный словарь из ОС-ки
    with open(path, 'r', encoding='utf-8') as f:
        return f.read().splitlines()


def get_list_of_keys(N):  # генерируем список ключей
    keys = []
    for i in range(N):
        keys.append(random.randint(1, 100))
    return keys


words = get_list_of_words('/usr/share/dict/words')
values = [random.choice(words) for _ in range(100)]  # генерируем список значений
N = 100
combined = dict(zip(get_list_of_keys(N), values))  # объединяем оба списка в словарь
print(combined)
for keys in combined:  # выводим попарно ключ - значение
    print(keys, combined[keys])
combined.clear()  # erase whole dictionary
