s = set()
g = set()
num_s_elements = int(input())
for _ in range(num_s_elements):
    s.add(input())

num_g_groups = int(input())
for _ in range(num_g_groups):
    num_g_elements = int(input())
    for _ in range(num_g_elements):
        g.add(input())

difference = sorted(s - g)

print(*difference, sep='\n')