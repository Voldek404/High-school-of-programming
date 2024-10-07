def convert_images(ext, output_extension):
    r = scan_dir(".", ext, False)
    for file in r[0]:
        image = Image.open(file)

        draw = ImageDraw.Draw(image)
        width, height = image.size
        square_size = min(width, height) // 2
        left = (width - square_size) // 2
        top = (height - square_size) // 2
        right = left + square_size
        bottom = top + square_size
        draw.rectangle((left, top, right, bottom), outline='black')

        font = ImageFont.truetype('arial.ttf', size=50)
        text = "Hello,\nWorld!"
        text_width, text_height = font.getsize(text)
        x = (width - text_width) // 2
        y = (height - text_height) // 2
        draw.text((x, y), text, fill='black', font=font, align='center')

        basename = os.path.splitext(file)[0]
        output_file = basename + '.' + output_extension
        image.save(output_file)