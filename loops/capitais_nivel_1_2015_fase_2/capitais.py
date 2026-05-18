import sys
from collections import deque

n = int(sys.stdin.readline())
g = [[] for _ in range(n + 1)]
for _ in range(n - 1):
    u, v = map(int, sys.stdin.readline().split())
    g[u].append(v)
    g[v].append(u)

leaves = [i for i in range(1, n + 1) if len(g[i]) == 1]

dist = [-1] * (n + 1)
src = [0] * (n + 1)
q = deque()

for leaf in leaves:
    dist[leaf] = 0
    src[leaf] = leaf
    q.append(leaf)

ans = n
while q:
    u = q.popleft()
    for v in g[u]:
        if dist[v] == -1:
            dist[v] = dist[u] + 1
            src[v] = src[u]
            q.append(v)
        elif src[v] != src[u]:
            ans = dist[u] + dist[v] + 1
            q.clear()
            break

print(ans)
