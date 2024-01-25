letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
shift = int(input())
sms = input().upper()
cipher = ''
for char in sms:
    if char in letters:
        index = letters.find(char)
        new_index = (index + shift) % len(letters)
        cipher += letters[new_index]
    else:
        cipher += char
print(cipher)