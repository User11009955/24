person_set = set()
pause_set = set()
n = int(input())
m = int(input())
k = int(input())
count = 0
for i in range(n + m + k):
    name = input()
    if name in person_set:
        count += 1
        pause_set.add(name)
    person_set.add(name)
if (n == k == m) and len(person_set) == n:
    print('NO')
else:
    if len(pause_set) + count > 0:
        if ((len(pause_set) + count) % 2 != 0):
            print((len(pause_set) + count) % 2)
        else:
            print((len(pause_set) + count) // 2)
    else:
        print('NO')