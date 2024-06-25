from zipfile import ZipFile
import os


def zip_insert(name, extension):
    if len(os.listdir(os.getcwd())) == 0: # проверка на пустой каталог
        print("Directory is empty")
    else:
        print("Directory is not empty")
    with ZipFile(name, 'w') as testzip: # создание рабочего архива
        for root, dirs, files in os.walk(os.getcwd()):
            for file in files:
                if file.endswith(extension): #Внесение в архив файлов по признаку расширения
                    testzip.write(os.path.join(root, file))
    return testzip.filename


name = 'test.zip'
extension = '.odg'
print(zip_insert(name, extension))
