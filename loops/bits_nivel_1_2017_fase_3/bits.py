MOD = 10**9 + 7
n, k = map(int, input().split())
dp = [0] * k
dp[0] = 1
for _ in range(n):
    ndp = [0] * k
    for j in range(k):
        ndp[0] = (ndp[0] + dp[j]) % MOD
    for j in range(1, k):
        ndp[j] = dp[j - 1]
    dp = ndp
print(sum(dp) % MOD)
