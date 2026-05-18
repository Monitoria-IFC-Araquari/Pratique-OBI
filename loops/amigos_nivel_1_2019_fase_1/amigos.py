n = int(input())
a = list(map(int, input().split()))
best = 0
best_j = a[0]
for i in range(1, n):
    val = a[i] + i + best_j
    if val > best:
        best = val
    cur = a[i] - i
    if cur > best_j:
        best_j = cur
print(best)
