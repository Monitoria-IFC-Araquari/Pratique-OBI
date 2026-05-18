l, c = map(int, input().split())
p = int(input())
pretas = set()
for _ in range(p):
    x, y = map(int, input().split())
    pretas.add((x - 1, y - 1))

grid = [[0] * c for _ in range(l)]
for i in range(l):
    for j in range(c):
        grid[i][j] = 1

for i, j in pretas:
    grid[i][j] = 2

candidatas = []
id_cell = {}
for i in range(l):
    for j in range(c):
        if grid[i][j] == 2:
            continue
        ok = False
        for di, dj in ((-1,0),(1,0),(0,-1),(0,1)):
            ni, nj = i + di, j + dj
            if 0 <= ni < l and 0 <= nj < c and grid[ni][nj] == 2:
                ok = True
                break
        if ok:
            candidatas.append((i, j))
            id_cell[(i, j)] = len(candidatas) - 1

n = len(candidatas)
g = [[] for _ in range(n)]
for i, j in candidatas:
    ui = id_cell[(i, j)]
    for di, dj in ((-1,0),(1,0),(0,-1),(0,1)):
        ni, nj = i + di, j + dj
        if (ni, nj) in id_cell:
            vi = id_cell[(ni, nj)]
            if (i + j) % 2 == 0:
                g[ui].append(vi)

match = [-1] * n
vis = [False] * n

def dfs(u):
    if vis[u]:
        return False
    vis[u] = True
    for v in g[u]:
        if match[v] == -1 or dfs(match[v]):
            match[v] = u
            return True
    return False

matching = 0
for u in range(n):
    ci, cj = candidatas[u]
    if (ci + cj) % 2 == 0:
        vis = [False] * n
        if dfs(u):
            matching += 1

print(n - matching)
