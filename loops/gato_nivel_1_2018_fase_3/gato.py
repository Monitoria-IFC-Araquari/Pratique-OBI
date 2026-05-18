from collections import deque

L, C = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(L)]

if grid[0][0] == 0 or grid[L - 1][C - 1] == 0:
    print(-1)
else:
    dist = [[-1] * C for _ in range(L)]
    q = deque()
    dist[0][0] = 0
    q.append((0, 0))
    while q:
        i, j = q.popleft()
        if i == L - 1 and j == C - 1:
            print(dist[i][j])
            break
        for di in range(-2, 3):
            for dj in range(-2, 3):
                if di == 0 and dj == 0:
                    continue
                ni, nj = i + di, j + dj
                if 0 <= ni < L and 0 <= nj < C and grid[ni][nj] == 1 and dist[ni][nj] == -1:
                    dist[ni][nj] = dist[i][j] + 1
                    q.append((ni, nj))
    else:
        print(-1)
