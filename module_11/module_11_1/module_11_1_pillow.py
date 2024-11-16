# Домашнее задание по теме "Обзор сторонних библиотек Python"

# pillow - обработать изображение, например, изменить его размер, применить
# эффекты и сохранить в другой формат.

from PIL import Image, ImageFilter
filename = "sarajevo.jpg"
with Image.open(filename) as img:
    img.load()
    low_res_img = img.reduce(2).filter(ImageFilter.EMBOSS)
    low_res_img.show()
    low_res_img.save("saraevo_bw.png")