n = int(input())
text = []
for i in range(n):
    text.append(input())
num_of_parts = int(input())

final_str = []
for i in range(num_of_parts):
    nums = int(input())
    if nums <= n:
        final_str.append(text[nums - 1])

for i in final_str:
    print(i)