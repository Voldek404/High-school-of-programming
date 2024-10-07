import os
from dir_oper_2 import get_list


def del_dir(path):
    res = get_list(path, ".*", False)
    if len(res[1]) > 0: # проверка на вложенные каталоги
        return False
    for f in res[0]:
        os.remove(path)  # перебор и удаление вложенных файлов
    os.rmdir(path)  # удаление пустого каталога
    return True

path = 'test_dir'  # определение расположения исходного каталога для работы функции
print(del_dir(path))
