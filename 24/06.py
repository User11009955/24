from PIL import Image


def make_preview(size, n_colors):
    # Открываем изображение
    image = Image.open('image.jpg')

    # Изменяем размер изображения
    resized_image = image.resize(size)

    # Уменьшаем количество цветов
    reduced_colors_image = resized_image.quantize(colors=n_colors)

    # Сохраняем результат в файле res.bmp
    reduced_colors_image.save('output_image/res.bmp')


# Вызываем функцию с указанными параметрами
make_preview((800, 600), 64)
