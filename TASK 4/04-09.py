spaces = int(input())
stars = 1

while spaces > 0:
    print(' ' * spaces + 'I' * stars)
    stars += 2
    spaces -= 1
