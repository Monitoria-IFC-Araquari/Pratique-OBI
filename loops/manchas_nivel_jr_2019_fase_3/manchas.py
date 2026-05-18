import sys
sys.setrecursionlimit(1 << 30)

N, M = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]

visited = [[False] * M for _ in range(N)]
ans = 0
for i in range(N):
    for j in range(M):
        if grid[i][j] == 1 and not visited[i][j]:
            ans += 1
            stack = [(i, j)]
            visited[i][j] = True
            while stack:
                x, y = stack.pop()
                for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny] and grid[nx][ny] == 1:
                        visited[nx][ny] = True
                        stack.append((nx, ny))
print(ans)
