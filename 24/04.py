from PIL import Image, ImageFilter


def motion_blur(n):
    # Открываем изображение
    image = Image.open('image.jpg')

    # Поворачиваем изображение на 270 градусов против часовой стрелки
    rotated_image = image.rotate(270)

    # Обрабатываем изображение с помощью размытия Гаусса
    blurred_image = rotated_image.filter(ImageFilter.GaussianBlur(radius=n))

    # Сохраняем результат в файле res.jpg
    blurred_image.save('output_image/res.jpg')


# Вызываем функцию с параметром n
motion_blur(10)
