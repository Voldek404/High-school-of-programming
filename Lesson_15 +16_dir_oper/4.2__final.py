import os
from dir_oper import get_list

def del_dir(path):
    res = get_list('test_dir', '.odt', False)
    for f in res[0]:
        os.remove(os.path.join(path,f))
    os.rmdir(path)
    return True
print(del_dir('test_dir'))
