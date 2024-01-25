n = int(input())
vertical = 'ABCDEFGHI'
if n < 10:
    for i in range(n, 0, -1):
        for j in vertical[:n]:
            print(j, i, sep='', end=' ')
            if j == vertical[n - 1]:
                print()
else:
    print("Много")