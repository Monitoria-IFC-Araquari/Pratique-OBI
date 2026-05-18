N = int(input())
grid = [list(input().strip()) for _ in range(N)]
vis = [[0] * N for _ in range(N)]
dirs = {'>': (0, 1), '<': (0, -1), 'v': (1, 0), '^': (-1, 0)}
ans = 0
for i in range(N):
    for j in range(N):
        if vis[i][j]:
            continue
        path = []
        r, c = i, j
        win = True
        while 0 <= r < N and 0 <= c < N:
            if vis[r][c]:
                break
            vis[r][c] = 1
            path.append((r, c))
            dr, dc = dirs[grid[r][c]]
            r += dr
            c += dc
        if not (0 <= r < N and 0 <= c < N):
            win = False
        for r, c in path:
            vis[r][c] = 2 if win else 3
        if win:
            ans += len(path)
print(ans)
