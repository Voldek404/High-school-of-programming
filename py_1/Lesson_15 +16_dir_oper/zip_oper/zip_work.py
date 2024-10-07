from zipfile import ZipFile
from dir_oper_2 import get_list
import os


def zip_insert(name, extension):
    res = get_list(path, extension, False)
    if len(res[0]) == 0:  # check whether the directory is empty
        return None
    with ZipFile(name, 'w') as testzip:  # creating zip file
        for f in res[0]:
            testzip.write(f)
    return testzip.filename


path = os.getcwd()
name = 'test.zip'
extension = '.ods'
print(zip_insert(name, extension))
