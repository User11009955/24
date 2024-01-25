from collections import Counter

num_cases = int(input())
names = []
for _ in range(num_cases):
    num_names = int(input())
    for _ in range(num_names):
        name = input()
        names.append(name)
name_counter = Counter(names)
for name, count in name_counter.items():
    if count == num_cases:
        print(name)