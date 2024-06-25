import os


def rm_dir(path):
    if not os.path.exists(path):  # проверка существования каталога
        return False
    for root, dirs, files in os.walk(path):
        if dirs: # проверка наличия вложенных каталогов
            return False
        else:
            for file in files:
                file_path = os.path.join(root, file)
                os.remove(file_path)  #перебор и удаление вложенных файлов
            os.rmdir(path) # удаление пустого каталога
    return True


print(rm_dir('test_dir'))
