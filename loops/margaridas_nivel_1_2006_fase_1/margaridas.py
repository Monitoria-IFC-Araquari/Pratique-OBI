L, C, M, N = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(L)]

pref = [[0] * (C + 1) for _ in range(L + 1)]
for i in range(1, L + 1):
    row_sum = 0
    for j in range(1, C + 1):
        row_sum += grid[i - 1][j - 1]
        pref[i][j] = pref[i - 1][j] + row_sum

ans = 0
for i in range(M, L + 1, M):
    for j in range(N, C + 1, N):
        s = pref[i][j] - pref[i - M][j] - pref[i][j - N] + pref[i - M][j - N]
        if s > ans:
            ans = s
print(ans)
