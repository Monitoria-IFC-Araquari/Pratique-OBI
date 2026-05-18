C = int(input())
lajotas = input().strip()
INF = 10**9
dp = [INF] * C
dp[0] = 0
for i in range(C):
    if dp[i] == INF:
        continue
    for j in range(1, 4):
        ni = i + j
        if ni < C and lajotas[ni] == 'P':
            dp[ni] = min(dp[ni], dp[i] + 1)
print(dp[C - 1] if dp[C - 1] != INF else -1)
