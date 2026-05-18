import sys
sys.setrecursionlimit(300000)

r, c = map(int, input().split())
g = [list(input().strip()) for _ in range(r)]

vis = [[False] * c for _ in range(r)]

def dfs(i, j):
    stack = [(i, j)]
    vis[i][j] = True
    sheep = 0
    wolves = 0
    escape = False
    while stack:
        x, y = stack.pop()
        if g[x][y] == 'k':
            sheep += 1
        elif g[x][y] == 'v':
            wolves += 1
        for dx, dy in ((1,0),(-1,0),(0,1),(0,-1)):
            nx, ny = x + dx, y + dy
            if nx < 0 or nx >= r or ny < 0 or ny >= c:
                escape = True
                continue
            if g[nx][ny] != '#' and not vis[nx][ny]:
                vis[nx][ny] = True
                stack.append((nx, ny))
    if escape:
        return 0, 0
    if sheep > wolves:
        return sheep, 0
    else:
        return 0, wolves

total_s = 0
total_w = 0
for i in range(r):
    for j in range(c):
        if g[i][j] != '#' and not vis[i][j]:
            s, w = dfs(i, j)
            total_s += s
            total_w += w

print(total_s, total_w)
