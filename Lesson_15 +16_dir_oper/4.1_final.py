import os


def get_list(path, extention, flag):
    if flag:
        list_1 = []  # создаем список для имен файлов
        list_2 = []  # создаем список для имен каталогов
        for f in os.listdir(path):
            if os.path.isdir(os.path.join(path, f)):
                list_2.append(f)

            else:
                if  f.endswith(extention):
                    list_1.append(f)
        return [list_1, list_2]


path = os.getcwd()
extention = '.odt'
flag = True

print(get_list(path, extention, flag))

