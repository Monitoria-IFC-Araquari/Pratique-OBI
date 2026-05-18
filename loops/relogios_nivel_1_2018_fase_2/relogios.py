from collections import deque
L, C, K = map(int, input().split())
grid = []
for _ in range(L):
    row = list(map(int, input().split()))
    grid.append(row)
sr = sc = tr = tc = 0
for i in range(L):
    for j in range(C):
        if grid[i][j] == 3:
            sr, sc = i, j
        elif grid[i][j] == 4:
            tr, tc = i, j
dist = [[-1] * C for _ in range(L)]
q = deque()
dist[sr][sc] = 0
q.append((sr, sc))
dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
while q:
    r, c = q.popleft()
    if (r, c) == (tr, tc):
        print(dist[r][c])
        break
    for dr, dc in dirs:
        nr, nc = r + dr, c + dc
        if not (0 <= nr < L and 0 <= nc < C):
            continue
        v = grid[nr][nc]
        if v == 2:
            continue
        nd = dist[r][c] + 1
        if 0 <= v < K and nd % K != v:
            continue
        if dist[nr][nc] == -1:
            dist[nr][nc] = nd
            q.append((nr, nc))
else:
    print(-1)
