n = int(input())
INF = 10**15
dist = [[0] * n for _ in range(n)]
for _ in range(n * (n - 1) // 2):
    a, b, t = map(int, input().split())
    a -= 1
    b -= 1
    dist[a][b] = t
    dist[b][a] = t

if n == 1:
    print(0)
elif n == 2:
    print(dist[0][1])
else:
    dp = [[INF] * n for _ in range(n)]
    dp[1][0] = dist[0][1]
    for i in range(2, n):
        for j in range(i - 1):
            dp[i][j] = dp[i - 1][j] + dist[i - 1][i]
        best = INF
        for k in range(i - 1):
            cand = dp[i - 1][k] + dist[k][i]
            if cand < best:
                best = cand
        dp[i][i - 1] = best
    ans = min(dp[n - 1][j] for j in range(n - 1))
    print(ans)
