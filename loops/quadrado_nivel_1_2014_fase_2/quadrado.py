N = int(input())
grid = [list(map(int, input().split())) for _ in range(N)]
M = 0
for row in grid:
    if 0 not in row:
        M = sum(row)
        break
if M == 0:
    for j in range(N):
        col = [grid[i][j] for i in range(N)]
        if 0 not in col:
            M = sum(col)
            break
for i in range(N):
    for j in range(N):
        if grid[i][j] == 0:
            grid[i][j] = M - sum(grid[i])
for row in grid:
    print(' '.join(map(str, row)))
