n, e, s, m = map(int, input().split())
edges = [[] for _ in range(n)]
for _ in range(m):
    a, b, t = map(int, input().split())
    edges[a].append((b, t))

INF = 10**9
dist = [[INF] * 3 for _ in range(n)]
from collections import deque
q = deque()
if any(t == 1 and 0 % 3 == 0 for _, t in edges[e]):
    dist[e][0] = 0
    q.append((e, 0))

while q:
    u, mod = q.popleft()
    d = dist[u][mod]
    for v, t in edges[u]:
        if (t == 1 and mod == 0) or (t == 0 and mod != 0):
            nd = d + 1
            nm = nd % 3
            if nd < dist[v][nm]:
                dist[v][nm] = nd
                q.append((v, nm))

ans = min(dist[s])
print(ans if ans != INF else '*')
