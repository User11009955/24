def find_cat():
    num_rows = int(input("Введите количество строк: "))
    cat_found = "НЕТ"

    for _ in range(num_rows):
        row = input("Введите строку: ")
        row = row.lower()
        last_index_cat = row.rfind('кот')
        last_index_dog = row.rfind('пёс')
        if last_index_cat != -1 and last_index_dog != -1 and last_index_cat > last_index_dog:
            cat_found = "МЯУ"
        elif last_index_cat != -1 and last_index_dog == -1:
            cat_found = "МЯУ"
        else:
            cat_found = "НЕТ"
    return cat_found


print(find_cat())