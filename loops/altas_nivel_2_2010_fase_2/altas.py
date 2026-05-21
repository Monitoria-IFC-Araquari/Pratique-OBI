n, k = map(int, input().split())

dp = [0] * (k + 1)

testes = 0

while dp[k] < n:
    testes += 1

    for i in range(k, 0, -1):
        dp[i] = dp[i] + dp[i - 1] + 1

print(testes)