from PIL import Image


def transparency(filename1, filename2):
    # Загрузка изображений
    image1 = Image.open(filename1)
    image2 = Image.open(filename2)

    # Создание нового изображения
    blended_image = Image.new("RGB", image1.size)

    # Получение данных пикселей для обоих изображений
    pixels1 = image1.load()
    pixels2 = image2.load()

    # Обработка каждого пикселя и смешивание изображений
    for x in range(blended_image.width):
        for y in range(blended_image.height):
            r1, g1, b1 = pixels1[x, y]
            r2, g2, b2 = pixels2[x, y]

            # Вычисление новых значений компонентов цвета
            r = int(0.5 * r1 + 0.5 * r2)
            g = int(0.5 * g1 + 0.5 * g2)
            b = int(0.5 * b1 + 0.5 * b2)

            blended_image.putpixel((x, y), (r, g, b))

    blended_image.save('output_image/fish_space.jpg')  # Отображение результирующего изображения


transparency('fish.jpg', 'space.jpg')
