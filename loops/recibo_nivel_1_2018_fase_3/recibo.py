R, K = map(int, input().split())
dp = [[0] * (R + 1) for _ in range(K + 1)]
dp[0][0] = 1
for price in range(1, R + 1):
    for k in range(K, 0, -1):
        for r in range(price, R + 1):
            dp[k][r] += dp[k - 1][r - price]
print(dp[K][R])
