import sys

n_str = sys.stdin.readline().strip()
s = sys.stdin.readline().strip()
mod = 1000000007

if len(n_str) > 100:
    max_val = 10 ** 100
else:
    max_val = int(n_str)

m = len(s)
dp = [0] * (m + 1)
dp[0] = 1

for i in range(1, m + 1):
    for j in range(i - 1, max(-1, i - 101), -1):
        if s[j] == '0':
            if j < i - 1:
                break
            continue
        num = int(s[j:i])
        if num > max_val:
            break
        dp[i] = (dp[i] + dp[j]) % mod

print(dp[m] % mod)
