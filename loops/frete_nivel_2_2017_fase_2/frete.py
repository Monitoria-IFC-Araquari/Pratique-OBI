import heapq

N, M = map(int, input().split())
adj = [[] for _ in range(N)]
for _ in range(M):
    A, B, C = map(int, input().split())
    adj[A - 1].append((B - 1, C))
    adj[B - 1].append((A - 1, C))
dist = [10**9] * N
dist[0] = 0
pq = [(0, 0)]
while pq:
    d, v = heapq.heappop(pq)
    if d > dist[v]:
        continue
    for u, w in adj[v]:
        nd = d + w
        if nd < dist[u]:
            dist[u] = nd
            heapq.heappush(pq, (nd, u))
print(dist[N - 1])
