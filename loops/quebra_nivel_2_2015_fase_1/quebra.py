N, E, D = map(int, input().split())
g = [[] for _ in range(N)]
deg = [0] * N
for _ in range(E):
    a, b = map(int, input().split())
    g[a - 1].append(b - 1)
    deg[b - 1] += 1
for _ in range(D):
    a, b = map(int, input().split())
    g[b - 1].append(a - 1)
    deg[a - 1] += 1
q = [i for i in range(N) if deg[i] == 0]
order = []
while q:
    u = q.pop()
    order.append(u)
    for v in g[u]:
        deg[v] -= 1
        if deg[v] == 0:
            q.append(v)
pos = [0] * N
for i, u in enumerate(order):
    pos[u] = i
print(' '.join(str(pos[i] + 1) for i in range(N)))
