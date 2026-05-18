n = int(input())
si, sj = map(int, input().split())
si -= 1
sj -= 1
grid = [list(map(int, input().split())) for _ in range(n)]

dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

visited = [[False] * n for _ in range(n)]

def dfs(i, j):
    visited[i][j] = True
    for d in range(4):
        ni = i + dr[d]
        nj = j + dc[d]
        if 0 <= ni < n and 0 <= nj < n and not visited[ni][nj] and grid[ni][nj] >= grid[i][j]:
            dfs(ni, nj)

dfs(si, sj)
print(sum(sum(row) for row in visited))
