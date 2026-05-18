n, m = map(int, input().split())
a = list(map(int, input().split()))

INF = 10**9
dp = {a[0], m - a[0]}
if 0 <= a[0] <= m:
    dp = {a[0]}
else:
    dp = set()

for i in range(1, n):
    ndp = set()
    for x in dp:
        v = a[i]
        if x <= v:
            ndp.add(v)
        if x <= m - v:
            ndp.add(m - v)
    dp = ndp
    if not dp:
        print(-1)
        break
else:
    print(min(dp) + sum(min(v, m - v) for v in a[1:]) if n == 1 else ...)
    # This needs more thought
    pass
