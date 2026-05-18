import sys
sys.setrecursionlimit(1000000)

n = int(input())
g = [list(input().strip()) for _ in range(n)]

rows = []
for i in range(n):
    segs = []
    for j in range(n):
        if g[i][j] == '*':
            if not segs or j != segs[-1][1] + 1:
                segs.append([j, j])
            else:
                segs[-1][1] = j
    if len(segs) > 1:
        print('N')
        sys.exit()
    rows.append(segs[0] if segs else None)

cols = []
for j in range(n):
    segs = []
    for i in range(n):
        if g[i][j] == '*':
            if not segs or i != segs[-1][1] + 1:
                segs.append([i, i])
            else:
                segs[-1][1] = i
    if len(segs) > 1:
        print('N')
        sys.exit()
    cols.append(segs[0] if segs else None)

start = None
total = 0
for i in range(n):
    for j in range(n):
        if g[i][j] == '*':
            total += 1
            if start is None:
                start = (i, j)

stack = [start]
vis = [[False] * n for _ in range(n)]
vis[start[0]][start[1]] = True
cnt = 0
while stack:
    x, y = stack.pop()
    cnt += 1
    for dx, dy in ((1,0),(-1,0),(0,1),(0,-1)):
        nx, ny = x + dx, y + dy
        if 0 <= nx < n and 0 <= ny < n and g[nx][ny] == '*' and not vis[nx][ny]:
            vis[nx][ny] = True
            stack.append((nx, ny))

print('S' if cnt == total else 'N')
