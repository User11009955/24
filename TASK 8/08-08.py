a = input()
count = 0
max_count = 0
for i in a:
    if i == 'о':
        count += 1
    else:
        count = 0
    if count > max_count:
        max_count = count
print(max_count)