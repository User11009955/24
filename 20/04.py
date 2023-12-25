import sys


print(sum(1 for i in sys.stdin.read().split('\n') if i.strip() and i.strip()[0] == '#'))