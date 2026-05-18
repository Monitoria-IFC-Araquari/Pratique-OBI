import heapq

n, m = map(int, input().split())
g = [[] for _ in range(n)]
for _ in range(m):
    u, v, p = map(int, input().split())
    u -= 1
    v -= 1
    g[u].append((v, p))
    g[v].append((u, p))
s = int(input()) - 1

INF = 10 ** 9
dist = [INF] * n
dist[s] = 0
pq = [(0, s)]
while pq:
    d, u = heapq.heappop(pq)
    if d != dist[u]:
        continue
    for v, p in g[u]:
        nd = d + p
        if nd < dist[v]:
            dist[v] = nd
            heapq.heappush(pq, (nd, v))

maxd = -1
mind = INF
for i in range(n):
    if i != s:
        if dist[i] > maxd:
            maxd = dist[i]
        if dist[i] < mind:
            mind = dist[i]
print(maxd - mind)
