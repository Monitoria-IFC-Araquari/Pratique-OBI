n, m = map(int, input().split())
a = list(map(int, input().split()))
INF = 10**18
dp0 = 0
dp1 = 0
v0 = a[0]
v1 = m - a[0]
ok0 = True
ok1 = a[0] != m - a[0]
for i in range(1, n):
    cur_v0 = a[i]
    cur_v1 = m - a[i]
    same = cur_v0 == cur_v1
    ndp0 = INF
    ndp1 = INF
    if ok0 and cur_v0 >= v0:
        ndp0 = min(ndp0, dp0 + cur_v0)
    if ok1 and cur_v0 >= v1:
        ndp0 = min(ndp0, dp1 + cur_v0)
    if not same:
        if ok0 and cur_v1 >= v0:
            ndp1 = min(ndp1, dp0 + cur_v1)
        if ok1 and cur_v1 >= v1:
            ndp1 = min(ndp1, dp1 + cur_v1)
    v0, v1 = cur_v0, cur_v1
    ok0 = ndp0 < INF
    ok1 = ndp1 < INF
    dp0, dp1 = ndp0, ndp1
ans = min(dp0, dp1) if ok0 or ok1 else -1
if ans >= INF:
    ans = -1
print(ans)
