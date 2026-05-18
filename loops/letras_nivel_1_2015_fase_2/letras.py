s = input().strip()
dp = [0] * 26
for ch in s:
    c = ord(ch) - 65
    best = 0
    for i in range(c + 1):
        if dp[i] > best:
            best = dp[i]
    dp[c] = best + 1
print(max(dp))
