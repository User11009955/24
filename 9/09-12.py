n = input()
s = []
s_indices = []
total_difference = 0
lot, total_sum = int(n[:4]), int(n[4:])
for i in range(lot):
    a = input()
    price, quantity, summ = int(a[0:7]), int(a[8:12]), int(a[13:18])
    if price * quantity != summ:
        s_indices.append(i + 1)
    calculated_sum = quantity * price
    s.append(calculated_sum)
for i in s:
    total_difference += i
print(total_sum - total_difference)
for i in s_indices:
    print(i, end=' ')