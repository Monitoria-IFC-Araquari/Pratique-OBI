from collections import deque

t, l, o, d = map(int, input().split())
lines = []
for _ in range(l):
    data = list(map(int, input().split()))
    lines.append(set(data[1:]))

adj = [[] for _ in range(t + l)]
for i in range(l):
    for term in lines[i]:
        adj[term - 1].append(t + i)
        adj[t + i].append(term - 1)

dist = [-1] * (t + l)
q = deque([o - 1])
dist[o - 1] = 0
while q:
    u = q.popleft()
    if u == d - 1:
        print(dist[u] // 2)
        break
    for v in adj[u]:
        if dist[v] == -1:
            dist[v] = dist[u] + 1
            q.append(v)
