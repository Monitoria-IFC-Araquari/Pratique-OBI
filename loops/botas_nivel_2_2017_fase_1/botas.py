from collections import defaultdict
n = int(input())
cnt = defaultdict(lambda: [0, 0])
for _ in range(n):
    m, l = input().split()
    m = int(m)
    cnt[m][l == 'D'] += 1
total = 0
for d, e in cnt.values():
    total += min(d, e)
print(total)
