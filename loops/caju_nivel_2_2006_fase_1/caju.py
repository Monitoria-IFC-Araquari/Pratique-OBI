l, c, m, n = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(l)]

ps = [[0] * (c + 1) for _ in range(l + 1)]
for i in range(l):
    row = grid[i]
    ps_row = ps[i + 1]
    ps_prev = ps[i]
    s = 0
    for j in range(c):
        s += row[j]
        ps_row[j + 1] = ps_prev[j + 1] + s

best = 0
for i in range(l - m + 1):
    for j in range(c - n + 1):
        val = ps[i + m][j + n] - ps[i][j + n] - ps[i + m][j] + ps[i][j]
        if val > best:
            best = val
print(best)
