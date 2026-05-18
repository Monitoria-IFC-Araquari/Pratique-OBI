import sys
import heapq

INF = 10 ** 18

n, m, c, k = map(int, sys.stdin.readline().split())
people = [int(x) - 1 for x in sys.stdin.readline().split()]
adj = [[] for _ in range(n)]
for _ in range(m):
    a, b, d = map(int, sys.stdin.readline().split())
    a -= 1
    b -= 1
    adj[a].append((b, d))

dist_from_n = [INF] * n
dist_from_n[n - 1] = 0
pq = [(0, n - 1)]
while pq:
    d, u = heapq.heappop(pq)
    if d != dist_from_n[u]:
        continue
    for v, w in adj[u]:
        if dist_from_n[v] > d + w:
            dist_from_n[v] = d + w
            heapq.heappush(pq, (dist_from_n[v], v))

person_set = set(people)
person_dist = [INF] * n
for p in people:
    person_dist[p] = 0

pq = [(0, p) for p in people]
heapq.heapify(pq)
while pq:
    d, u = heapq.heappop(pq)
    if d != person_dist[u]:
        continue
    for v, w in adj[u]:
        if person_dist[v] > d + w:
            person_dist[v] = d + w
            heapq.heappush(pq, (person_dist[v], v))

alert = [False] * n
pq = [(0, 0)]
while pq:
    d, u = heapq.heappop(pq)
    if alert[u]:
        continue
    alert[u] = True
    for v, w in adj[u]:
        if d + w <= k and not alert[v]:
            heapq.heappush(pq, (d + w, v))

ans = INF
for p in people:
    if alert[p] and dist_from_n[p] != INF:
        t = max(0, dist_from_n[p] - k)
        if t < ans:
            ans = t

print(-1 if ans == INF else ans)
