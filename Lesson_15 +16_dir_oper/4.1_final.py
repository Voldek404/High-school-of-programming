import os

def get_list(path, extention, flag):
    list_1 = []  # создаем список для имен файлов
    list_2 = []
    for f in os.listdir(path):
         if os.path.isfile(os.path.join(path, f)):
             if f.endswith(extention):
                list_1.append(f)
         elif os.path.isdir(os.path.join(path, f)):
            list_2.append(f)  # добавляем элемент в list_2
            if flag:
                results = get_list(os.path.join(path, f), extention, False)
                for item in results:
                    list_1.append(item)

    return [list_1,list_2]


path = os.getcwd()
extention = '.odt'
flag = True
count = 0

print(get_list(path, extention, flag))
