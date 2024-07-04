import os


def get_list(path, extention, flag, count):
    if flag:
        list_1 = []  # создаем список для имен файлов
        list_3 = []
        for f in os.listdir(path):
            if os.path.isfile(os.path.join(path, f)):
                if f.endswith(extention):
                    list_1.append(f)
            elif os.path.isdir(os.path.join(path, f)) and count < 2:
                list_3.append(f)
                list_2 = get_list(os.path.join(path, f), extention, True, count + 1)
                for item in list_2:
                    list_1.append(item)
        return list_1, list_3


path = os.getcwd()
extention = '.odt'
flag = True
count = 0

print(get_list(path, extention, flag, count))
