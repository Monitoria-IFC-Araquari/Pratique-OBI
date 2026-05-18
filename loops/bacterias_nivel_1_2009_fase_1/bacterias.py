import math

n = int(input())
best_idx = 0
best_log = -1.0
for i in range(n):
    d, c = map(int, input().split())
    cur_log = c * math.log(d)
    if cur_log > best_log:
        best_log = cur_log
        best_idx = i
print(best_idx)
