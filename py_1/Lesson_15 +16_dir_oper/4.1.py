import os


def get_list(path, extention, flag):
    list_1 = []  # создаем список для имен файлов
    list_2 = []  # создаем список для имен каталогов
    if not os.path.exists(path):
        return None, None  # возвращаем None, если путь не существует
    if not os.listdir(path):  # проверяем, пуст ли каталог
        return None, None  # возвращаем пустые списки, если каталог пуст
    for root, dirs, files in os.walk(path, topdown=True):  # Параметр topdown для начала прохода от корня каталога
        for file in files:
            if file.endswith(extention):
                list_1.append(file)
            break  # ограничиваем проход цикла для каталогов первого уровня вложенности
    for root, dirs, files in os.walk(path, topdown=True):
        for dir in dirs:
            list_2.append(dir)
        break  # ограничиваем проход цикла для каталогов первого уровня вложенности
    return list_1, list_2


path = os.getcwd()  # определение расположения исходного каталога для работы функции
extention = '.odt'
flag = True
print(get_list(path, extention, flag))
