def solve():
    v, m = map(int, input().split())
    moedas = list(map(int, input().split()))
    dp = [False] * (v + 1)
    dp[0] = True
    for moeda in moedas:
        for j in range(v, moeda - 1, -1):
            if dp[j - moeda]:
                dp[j] = True
    print('S' if dp[v] else 'N')

if __name__ == '__main__':
    solve()
