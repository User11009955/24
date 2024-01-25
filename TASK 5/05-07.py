count = int(input())
euro = "Евразия"
osta = "Остазия"

for i in range(count):
    question = input()

    if question == "С кем война?":
        print(euro)
    elif question == "С кем мир?":
        print(osta)
    elif question == "Меняем":
        temp = euro
        euro = osta
        osta = temp