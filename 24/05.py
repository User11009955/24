import wave


def break_the_silence():
    # Открываем исходный файл в режиме чтения
    with wave.open('in.wav', 'rb') as src_file:
        # Получаем параметры аудиофайла
        nchannels, sampwidth, framerate, nframes, comptype, compname = src_file.getparams()

        # Открываем новый аудиофайл для записи
    with wave.open('output_image/out.wav', 'wb') as dest_file:
        # Устанавливаем параметры нового аудиофайла
        dest_file.setparams((nchannels, sampwidth, framerate, 0, comptype, compname))

    # Читаем и записываем каждый фрейм из исходного файла
    for i in range(nframes):
        frame = src_file.readframes(i)  # Читаем фрейм из исходного файла

        # Если амплитуда звука в пределах [-5, 5], считаем фрейм тихим и не записываем его
        if all(-5 <= samp <= 5 for samp in frame):
            continue

        # Записываем фрейм в новый файл
        dest_file.writeframes(frame)


break_the_silence()
