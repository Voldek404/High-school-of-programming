import os


def arrayOfAllFiles(targetDirectory):
    if not os.path.exists(targetDirectory):
        raise ValueError("Каталог не существует")
    if not os.listdir(targetDirectory):
        raise ValueError("Каталог пуст")
    arrayOfNames = []
    for item in os.listdir(targetDirectory):
        fullPath = os.path.join(targetDirectory, item)
        if os.path.isfile(fullPath):
            if item.endswith(fileExtention):
                arrayOfNames.append(item)
        elif os.path.isdir(fullPath):
            arrayOfNames.extend(arrayOfAllFiles(fullPath))
    return arrayOfNames


targetDirectory = os.getcwd()
fileExtention = '' 
