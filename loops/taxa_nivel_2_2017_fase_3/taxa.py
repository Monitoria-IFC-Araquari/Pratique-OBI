N, F = map(float, input().split())
N = int(N)
vals = [0] * N
for i in range(N):
    vals[i] = float(input())
INF = 10**9
dp = [INF] * (N + 1)
dp[0] = 0
pref = [0]
for v in vals:
    pref.append(pref[-1] + v)
for i in range(1, N + 1):
    for j in range(i):
        sum_val = pref[i] - pref[j]
        cost = sum_val * (F / 100)
        dp[i] = min(dp[i], dp[j] + cost + 1)
print(f"{dp[N]:.2f}")
