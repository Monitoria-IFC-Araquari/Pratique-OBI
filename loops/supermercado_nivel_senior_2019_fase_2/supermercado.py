N, G = map(int, input().split())
items = []
for _ in range(N):
    p, g = map(int, input().split())
    items.append((p, g))
dp = [0] * (G + 1)
for p, g in items:
    for w in range(G, g - 1, -1):
        dp[w] = max(dp[w], dp[w - g] + p)
print(max(dp))
