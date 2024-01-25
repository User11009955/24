count = int(input())
total_iq = 0

for i in range(1, count + 1):
    iq = int(input())
    total_iq += iq
    average = total_iq / i

    if iq == average:
        print('0')
    elif iq > average:
        print('>')
    elif iq < average:
        print('<')