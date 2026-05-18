N, L, H = map(int, input().split())
s = list(map(int, input().split()))
m = list(map(int, input().split()))
INF = 10**15
dp = [-INF] * (H + 1)
ans = -INF
for i in range(N):
    ndp = [-INF] * (H + 1)
    if m[i] == 1:
        if dp[0] > -INF:
            ndp[1] = max(s[i], dp[0] + s[i])
        else:
            ndp[1] = s[i]
        for k in range(2, H + 1):
            if dp[k - 1] > -INF:
                ndp[k] = max(ndp[k], dp[k - 1] + s[i])
    else:
        if dp[0] > -INF:
            ndp[0] = max(s[i], dp[0] + s[i])
        else:
            ndp[0] = s[i]
        for k in range(1, H + 1):
            if dp[k] > -INF:
                ndp[k] = max(ndp[k], dp[k] + s[i])
    dp = ndp
    for k in range(L, H + 1):
        ans = max(ans, dp[k])
if L == 0:
    ans = max(ans, 0)
print(ans)
