import sys

def solve():
    n = int(sys.stdin.readline())
    s = sys.stdin.readline().strip()
    pal = [[False] * n for _ in range(n)]
    for i in range(n):
        pal[i][i] = True
    for i in range(n - 1):
        if s[i] == s[i+1]:
            pal[i][i+1] = True
    for length in range(3, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            if s[i] == s[j] and pal[i+1][j-1]:
                pal[i][j] = True
    INF = 10**9
    dp = [INF] * (n + 1)
    dp[0] = 0
    for i in range(1, n + 1):
        for j in range(i):
            if pal[j][i-1]:
                if dp[j] + 1 < dp[i]:
                    dp[i] = dp[j] + 1
    print(dp[n])

if __name__ == '__main__':
    solve()
