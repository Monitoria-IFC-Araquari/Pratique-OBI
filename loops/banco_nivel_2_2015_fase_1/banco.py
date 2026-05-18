S = int(input())
valores = [2, 5, 10, 20, 50, 100]
limites = list(map(int, input().split()))
dp = [0] * (S + 1)
dp[0] = 1
for valor, lim in zip(valores, limites):
    for s in range(S, -1, -1):
        if dp[s]:
            for q in range(1, lim + 1):
                ns = s + q * valor
                if ns > S:
                    break
                dp[ns] += dp[s]
print(dp[S])
