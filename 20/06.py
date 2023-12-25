# Не понимаю в чем смысл КодБуквы - КодБуквыA + 1, разве это как то отличается от складывания всех букв в слове и последующей сортировке по сумме?

import sys


def calculate_gematria(word):
    return sum(ord(letter) - ord('A') + 1 for letter in word.upper())


# Считываем список слов
words = []
for line in sys.stdin:
    word = line.strip()
    if not word:
        break
    words.append(word)

# Сортируем слова по их гематрии
sorted_words = sorted(words, key=lambda word: (calculate_gematria(word), word))

# Выводим отсортированные слова
for word in sorted_words:
    print(word)

