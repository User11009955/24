first = set()
second = set()

c = input()
while c != '':
    first.add(c)
    c = input()

c1 = input()
while c1 != '':
    second.add(c1)
    c1 = input()

intersection = first.intersection(second)

if not intersection:
    print("EMPTY")
else:
    for item in intersection:
        print(item)