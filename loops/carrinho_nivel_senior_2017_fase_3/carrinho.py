INF = float('inf')
n, d = input().split()
n = int(n)
d = float(d)
pos = []
cap = []
for _ in range(n):
    p, c = map(float, input().split())
    pos.append(p)
    cap.append(c)

dp = [0.0] * n
for i in range(1, n):
    best = INF
    for j in range(i):
        dist = pos[i] - pos[j]
        t = dp[j] + dist * dist / cap[j]
        if t < best:
            best = t
    dp[i] = best

ans = INF
for i in range(n):
    dist = d - pos[i]
    t = dp[i] + dist * dist / cap[i]
    if t < ans:
        ans = t

print(f'{ans:.3f}')
