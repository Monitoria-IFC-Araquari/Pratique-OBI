from collections import deque

N, M = map(int, input().split())
Xe, Ye = map(int, input().split())
Xs, Ys = map(int, input().split())

Xe -= 1; Ye -= 1; Xs -= 1; Ys -= 1

cabinets = [(i, j) for i in range(1, N - 1) for j in range(1, M - 1) if i % 2 == 0 and j % 2 == 0]

dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]

best = 0

def bfs(blocked):
    q = deque()
    q.append((Xe, Ye))
    dist = [[-1] * M for _ in range(N)]
    dist[Xe][Ye] = 1
    while q:
        i, j = q.popleft()
        if i == Xs and j == Ys:
            return dist[i][j]
        for di, dj in dirs:
            ni, nj = i + di, j + dj
            if 0 <= ni < N and 0 <= nj < M and dist[ni][nj] == -1 and not blocked[ni][nj]:
                dist[ni][nj] = dist[i][j] + 1
                q.append((ni, nj))
    return -1

def backtrack(idx, blocked):
    global best
    if idx == len(cabinets):
        d = bfs(blocked)
        if d > best:
            best = d
        return
    rem = len(cabinets) - idx
    if best >= N * M - 2 * rem:
        return
    i, j = cabinets[idx]
    blocked[i][j] = True
    for di, dj in dirs:
        ni, nj = i + di, j + dj
        if 0 <= ni < N and 0 <= nj < M and not (ni == Xe and nj == Ye) and not (ni == Xs and nj == Ys):
            blocked[ni][nj] = True
            backtrack(idx + 1, blocked)
            blocked[ni][nj] = False
    backtrack(idx + 1, blocked)
    blocked[i][j] = False

blocked = [[False] * M for _ in range(N)]
backtrack(0, blocked)
print(best)
