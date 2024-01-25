start = 1
end = 10000

for _ in range(10):
    mid = (start + end) // 2
    response = input(str(mid) + '\n')

    if response == '>':
        start = mid + 1
    elif response == '<':
        end = mid - 1
    elif response == '=':
        break
