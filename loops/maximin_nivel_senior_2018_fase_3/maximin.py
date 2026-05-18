N, L, R = map(int, input().split())
a = list(map(int, input().split()))
a.sort()

best = 0
for x in (L, R):
    d = min(abs(x - v) for v in a)
    if d > best:
        best = d

for i in range(N - 1):
    mid = (a[i] + a[i + 1]) // 2
    for x in (mid, mid + 1):
        if L <= x <= R:
            d = min(abs(x - v) for v in a)
            if d > best:
                best = d

print(best)
