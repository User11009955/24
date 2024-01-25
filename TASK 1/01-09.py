login = input("Введите ЛОГИН: ")
email = input("Введите EMAIL: ")
if "@" in login:
    print("Некорректный ЛОГИН")
elif "@" not in email:
    print("Некорректный EMAIL")
else:
    print("ОК")
