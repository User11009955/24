def process_words(num):
    new = set()
    for i in range(num):
        word = input()
        if word[:3].lower() == 'не ':
            word = word[3:]
        elif word[:3].lower() == 'не':
            word = word[2:]
        new.add(word)
    return new

num = int(input())
unique_words = process_words(num)
for word in unique_words:
    print(word)