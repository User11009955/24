n = int(input())
names = []
for i in range(n):
    names.append(input())

step = int(input("Step"))
rounds = int(input("Rounds"))

for j in range(rounds):
    del names[step-1::step]
print("".join(names))