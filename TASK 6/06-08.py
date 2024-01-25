num_men = int(input())
men_works = [input() for _ in range(num_men)]
result = 0
for example in set(men_works):
    count = 0
    for name in men_works:
        if example == name:
            count += 1
    if count > 1:
        result += count
print(result)