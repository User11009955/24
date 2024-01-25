count_days = 0
while True:
    temperature = float(input("Напишите нынешнее значение температуры: "))
    count_days += 1
    if temperature >= 22.0:
        break
count_weeks = count_days // 7
print(count_weeks, 'полных недель')
