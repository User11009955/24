words = input()
min_word = words
max_word = words
answer_yes = 'ДА'
answer_no = 'НЕТ'
while True:
    words = input()
    if words == 'стоп':
        if len(set(min_word) - set(max_word)) == 0:
            print(answer_yes)
            break
        else:
            print(answer_no)
            break
    if len(words) > len(max_word):
        max_word = words
    if len(words) < len(min_word):
        min_word = words