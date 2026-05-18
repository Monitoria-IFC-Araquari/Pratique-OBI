from collections import deque

n, m = map(int, input().split())
g = [list(input().strip()) for _ in range(n)]
q = deque()

for j in range(m):
    if g[0][j] == 'o':
        q.append((0, j))

while q:
    i, j = q.popleft()
    if i + 1 < n and g[i + 1][j] == '.':
        g[i + 1][j] = 'o'
        q.append((i + 1, j))
    if i + 1 < n and g[i + 1][j] == '#':
        if j - 1 >= 0 and g[i][j - 1] == '.':
            g[i][j - 1] = 'o'
            q.append((i, j - 1))
        if j + 1 < m and g[i][j + 1] == '.':
            g[i][j + 1] = 'o'
            q.append((i, j + 1))

for row in g:
    print(''.join(row))
