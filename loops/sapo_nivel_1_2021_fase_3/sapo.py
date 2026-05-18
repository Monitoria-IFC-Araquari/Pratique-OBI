from collections import deque
N, M, P = map(int, input().split())
grid = [[0] * M for _ in range(N)]
stones = []
for _ in range(P):
    C, L = map(int, input().split())
    grid[C - 1][L - 1] = 1
    stones.append((C - 1, L - 1))
SC, SL = map(int, input().split())
TC, TL = map(int, input().split())
SC -= 1
SL -= 1
TC -= 1
TL -= 1
q = deque()
q.append((SC, SL))
vis = [[False] * M for _ in range(N)]
vis[SC][SL] = True
dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
while q:
    r, c = q.popleft()
    if (r, c) == (TC, TL):
        print('S')
        break
    for dr, dc in dirs:
        for dist in range(1, 4):
            nr, nc = r + dr * dist, c + dc * dist
            if 0 <= nr < N and 0 <= nc < M and not vis[nr][nc] and grid[nr][nc] == 1:
                vis[nr][nc] = True
                q.append((nr, nc))
else:
    print('N')
