result = 1
for i in range(6):
    number = int(input("Введите целое число: "))
    if number != 0:
        result *= number
print("Произведение введенных чисел без учета нулей:", result)
