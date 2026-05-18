import sys
sys.setrecursionlimit(1000000)

n, m = map(int, input().split())
g = [list(map(int, input().split())) for _ in range(n)]

vis = [[False] * m for _ in range(n)]
ans = 0

for i in range(n):
    for j in range(m):
        if g[i][j] == 1 and not vis[i][j]:
            ans += 1
            stack = [(i, j)]
            vis[i][j] = True
            while stack:
                x, y = stack.pop()
                for dx, dy in ((1,0),(-1,0),(0,1),(0,-1)):
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < n and 0 <= ny < m and g[nx][ny] == 1 and not vis[nx][ny]:
                        vis[nx][ny] = True
                        stack.append((nx, ny))

print(ans)
