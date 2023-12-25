m = int(input())
excellent_students = []
for _ in range(m):
    n = int(input())
    for _ in range(n):
        student = int(input().split()[1])
        if student == 5:
            excellent_students.append(True)

print('ДА' if len(excellent_students) >= m else "НЕТ")
