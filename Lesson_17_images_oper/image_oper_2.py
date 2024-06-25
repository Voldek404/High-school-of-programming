import os
from PIL import Image, ImageDraw, ImageColor, ImageFont


def image_convert(path, extention_1, extention_2):
    count = 0
    for root, dirs, files in os.walk(path):
        for file in files:
            if file.endswith(extention_1):
                try:
                    im = Image.open(os.path.join(root, file))
                    im.save(os.path.join(root, file.replace(extention_1, extention_2)))
                    draw = ImageDraw.Draw(im)
                    # Вычисляем координаты центра изображения
                    width, height = im.size
                    center_x, center_y = width // 2, height // 2
                    draw.line([(center_x - 100, center_y - 100), (center_x + 100, center_y - 100)], fill=(255, 57, 229), width=5)
                    draw.line([(center_x + 100, center_y - 100), (center_x + 100, center_y + 100)], fill=(255, 57, 229), width=5)
                    draw.line([(center_x - 100, center_y + 100), (center_x - 100, center_y - 100)], fill=(255, 57, 229), width=5)
                    draw.line([(center_x - 100, center_y + 100), (center_x + 100, center_y +100)], fill=(255, 57, 229), width=5)
                    # Увеличиваем размер шрифта
                    font = ImageFont.load_default(45)
                    draw.multiline_text((center_x-50, center_y-50), "Hello,\nWorld!", fill=(255, 57, 229), font=font)
                    im.save(os.path.join(root, file.replace(extention_1, extention_2)))
                    im.show()
                    count += 1
                except Exception as e:
                    print(f"Error processing {file}: {e}")
    return print('Количество конвертированных изображений - ', count)


path = os.getcwd()  # определение расположения исходного каталога для работы функции
extention_1 = '.jpg'
extention_2 = '.png'
image_convert(path, extention_1, extention_2)
