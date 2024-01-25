n = int(input())
c = 0
found_kitten = False
for i in range(n):
    line = input()
    c += 1
    if 'кот' in line.lower():
        found_kitten = True
        index = line.lower().index('кот') + 1
        print(c, index)
        break
if not found_kitten:
    print(-1)
