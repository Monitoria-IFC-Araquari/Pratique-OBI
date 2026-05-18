import sys
sys.setrecursionlimit(1000000)

n, m = map(int, sys.stdin.readline().split())
g = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

si = sj = -1
for i in range(n):
    for j in range(m):
        if g[i][j] == 2:
            si, sj = i, j

def dfs(i, j, count):
    if g[i][j] == 3:
        return count
    g[i][j] = -1
    for di, dj in ((1,0),(-1,0),(0,1),(0,-1)):
        ni, nj = i + di, j + dj
        if 0 <= ni < n and 0 <= nj < m and (g[ni][nj] == 1 or g[ni][nj] == 3):
            res = dfs(ni, nj, count + 1)
            if res:
                return res
    return 0

print(dfs(si, sj, 1))
