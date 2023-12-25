from PIL import Image


def twist_image(input_file_name, output_file_name):
    # Загружаем изображение
    image = Image.open(input_file_name)

    # Разделяем изображение на две равные части по горизонтали
    width, height = image.size
    top_half = image.crop((0, 0, width, height // 2))
    bottom_half = image.crop((0, height // 2, width, height))

    # Разворачиваем каждую часть в другую сторону
    top_half = top_half.transpose(Image.ROTATE_180)
    bottom_half = bottom_half.transpose(Image.ROTATE_180)

    # Создаем новое изображение, объединяя развернутые части
    new_image = Image.new('RGB', (width, height))
    new_image.paste(top_half, (0, 0))
    new_image.paste(bottom_half, (0, height // 2))

    # Отображаем новое изображение
    new_image.save(output_file_name)


twist_image('statement-image.jpg', 'output_image/statement-image_1.jpg')
