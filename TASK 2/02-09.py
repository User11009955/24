height_1 = int(input())
height_2 = int(input())
height_3 = int(input())
print('\n'.join(str(i) for i in sorted([height_1, height_2, height_3], reverse=True)))
