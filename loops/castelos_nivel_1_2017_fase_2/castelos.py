import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())
g = [[] for _ in range(n + 1)]
for _ in range(n - 1):
    u, v = map(int, sys.stdin.readline().split())
    g[u].append(v)
    g[v].append(u)

color = [0] * (n + 1)

def paint(p, q, c):
    parent = [0] * (n + 1)
    qq = deque([p])
    parent[p] = -1
    while qq:
        u = qq.popleft()
        if u == q:
            break
        for v in g[u]:
            if v != parent[u]:
                parent[v] = u
                qq.append(v)
    u = q
    while u != -1:
        color[u] = c
        u = parent[u]

for _ in range(m):
    p, q, c = map(int, sys.stdin.readline().split())
    paint(p, q, c)

print(' '.join(str(color[i]) for i in range(1, n + 1)))
