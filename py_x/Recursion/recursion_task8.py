import os


def catalogueWalker(targetDirectory, arrayOfNames):
    for item in os.listdir(targetDirectory):
        fullPath = os.path.join(targetDirectory, item)
        if os.path.isfile(fullPath):
            if item.endswith(fileExtention):
                arrayOfNames.append(item)
        elif os.path.isdir(fullPath):
            catalogueWalker(fullPath, arrayOfNames)
    return arrayOfNames


def arrayOfAllFiles(targetDirectory):
    if not os.path.exists(targetDirectory):
        raise ValueError("Каталог не существует")
    if not os.listdir(targetDirectory):
        raise ValueError("Каталог пуст")
    return catalogueWalker(targetDirectory, [])


targetDirectory = os.getcwd()
fileExtention = ''
