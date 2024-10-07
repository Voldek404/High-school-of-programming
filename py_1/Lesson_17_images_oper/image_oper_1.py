import os
from PIL import Image, ImageDraw, ImageColor


def image_convert(path, extention_1, extention_2):
    count = 0
    for root, dirs, files in os.walk(path):
        for file in files:
            if file.endswith(extention_1):
                try:
                    im = Image.open(os.path.join(root, file))
                    im.save(os.path.join(root, file.replace(extention_1, extention_2)))

                    count += 1
                except Exception as e:
                    print(f"Error processing {file}: {e}")
    return print('Количество конвертированных изображений - ', count)


path = os.getcwd()  # определение расположения исходного каталога для работы функции
extention_1 = '.png'
extention_2 = '.bmp'
image_convert(path, extention_1, extention_2)
