def solve():
    n = int(input())
    pecas = input().split()
    MOD = 10007
    dp = [0] * (n + 2)
    dp[0] = 1
    for i in range(1, n + 1):
        if pecas[i - 1] == 'B':
            dp[i] = dp[i - 1]
        else:
            if i >= 2:
                dp[i] = (dp[i - 1] + dp[i - 2]) % MOD
            else:
                dp[i] = dp[i - 1]
    print(dp[n] % MOD)

if __name__ == '__main__':
    solve()
