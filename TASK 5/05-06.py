total_sum = 0
count = 1
number = 1

while number != 0:
    number = int(input())
    total_sum += number
    count += 1

    if total_sum >= 10:
        print(count - 1)
        break