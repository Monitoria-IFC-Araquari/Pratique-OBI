N = int(input())
grid = [list(map(int, input().split())) for _ in range(N)]
ops = [(0, -1), (0, 1), (1, 0), (-1, 0)]
while True:
    changed = False
    for i in range(N):
        for j in range(N):
            if grid[i][j] == 0:
                black = 0
                for di, dj in ops:
                    ni, nj = i + di, j + dj
                    if 0 <= ni < N and 0 <= nj < N and grid[ni][nj] == 1:
                        black += 1
                if black >= 2:
                    grid[i][j] = 1
                    changed = True
    if not changed:
        break
print(sum(row.count(0) for row in grid))
