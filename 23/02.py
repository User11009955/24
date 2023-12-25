from PIL import Image


def average_pixel_values(image_path):
    # Открываем изображение
    image = Image.open(image_path)

    # Получаем размер изображения
    width, height = image.size

    # Инициализируем переменные для суммирования компонент R, G и B
    sum_r = 0
    sum_g = 0
    sum_b = 0

    # Перебираем каждый пиксель изображения
    for y in range(height):
        for x in range(width):
            # Получаем значение цвета пикселя
            r, g, b = image.getpixel((x, y))

            # Суммируем цветовые компоненты R, G и B
            sum_r += r
            sum_g += g
            sum_b += b

    # Вычисляем средние значения цветовых компонент R, G и B
    average_r = sum_r // (width * height)
    average_g = sum_g // (width * height)
    average_b = sum_b // (width * height)

    # Выводим средние значения на экран
    print(average_r, average_g, average_b)


# Вызываем функцию с указанием пути к изображению
average_pixel_values('image.jpg')
