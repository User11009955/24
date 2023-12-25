import wave


def chip_and_dale(number):
    # Открываем исходный файл в режиме чтения
    with wave.open('in.wav', 'rb') as src_file:
        # Получаем параметры аудиофайла

        nchannels, sampwidth, framerate, nframes, comptype, compname = src_file.getparams()
    # Создаем новый аудиофайл для записи
    with wave.open('output_image/out.wav', 'wb') as dest_file:

        # Устанавливаем параметры нового аудиофайла
        dest_file.setparams((nchannels, sampwidth, framerate, nframes // number, comptype, compname))

        # Читаем и записываем каждый i-ый фрейм
        for i in range(nframes):
            frame = src_file.readframes(i)  # Читаем фрейм из исходного файла
            if i % number == 0:
                dest_file.writeframes(frame)  # Записываем фрейм в новый файл


chip_and_dale(2)
