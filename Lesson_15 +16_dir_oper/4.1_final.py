import os


def get_list(path):
    list_1 = []  # создаем список для имен файлов
    list_2 = []  # создаем список для имен каталогов
    for f in os.listdir(path):
        if os.path.isdir(os.path.join(path, f)):
            list_2.append(f)
        else:
            if f.endswith('.py'):
                list_1.append(f)
    return [list_1, list_2]


path = os.getcwd()

print(get_list(path))
