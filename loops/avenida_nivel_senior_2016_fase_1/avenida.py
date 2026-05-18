N, M = map(int, input().split())
col_sum = [0] * M
for _ in range(N):
    row = list(map(int, input().split()))
    for j in range(M):
        col_sum[j] += row[j]

prefix = 0
total = sum(col_sum)
best = total
for j in range(M - 1):
    prefix += col_sum[j]
    cost = min(prefix, total - prefix)
    if cost < best:
        best = cost
print(best)
