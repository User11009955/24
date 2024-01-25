flag = False
num = int(input())
found_system = []
input_system = []
for i in range(num):
    found_system.append(input())
num1 = int(input())
for i in range(num1):
    input_system.append(input())
for i in found_system:
    for j in input_system:
        if j in i:
            flag = True
        else:
            flag = False
            break
    if flag:
        print(i)
