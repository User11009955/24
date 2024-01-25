num = int(input())
while num >= 0:
    print(f"Осталось секунд: {num}")
    num -= 1
    if num < 0:
        print("ПУСК!")
