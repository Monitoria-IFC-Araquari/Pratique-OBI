N = int(input())
vals = [int(input()) for _ in range(N)]
total = sum(vals)
dp = [False] * (total // 2 + 1)
dp[0] = True
for v in vals:
    for s in range(total // 2, v - 1, -1):
        if dp[s - v]:
            dp[s] = True
best = 0
for s in range(total // 2 + 1):
    if dp[s]:
        best = s
print(total - 2 * best)
