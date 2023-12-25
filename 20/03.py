import sys


def average_height():
    average = 0
    a = input()
    if a.rstrip('\n') == '':
        return -1
    else:
        average += int(a)
    n = 1
    for line in sys.stdin:
        n += 1
        if line.rstrip('\n') == '':
            return average / (n - 1)
        else:
            average += int(line.rstrip('\n'))


print(average_height())
