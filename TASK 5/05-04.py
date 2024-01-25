count = int(input())
has_cat = False

for i in range(count):
    string = input()

    if "кот" in string or "Кот" in string:
        has_cat = True
        print("мяу")
        break

if not has_cat:
    print("нет")