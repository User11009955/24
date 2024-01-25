start_number = int(input("Введите начальное число: "))
end_number = int(input("Введите конечное число: "))

for number in range(start_number, end_number + 1):
    if number % 5 == 0 and number % 3 == 0:
        print("FizzBuzz")
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        print(number)