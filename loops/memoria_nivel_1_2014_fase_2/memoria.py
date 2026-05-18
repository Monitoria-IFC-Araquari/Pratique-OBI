import sys
sys.setrecursionlimit(1 << 30)

N = int(input())
vals = list(map(int, input().split()))
pairs = [[] for _ in range(N // 2 + 1)]
for i, v in enumerate(vals, 1):
    pairs[v].append(i)

adj = [[] for _ in range(N + 1)]
for _ in range(N - 1):
    a, b = map(int, input().split())
    adj[a].append(b)
    adj[b].append(a)

LOG = 17
parent = [[0] * (N + 1) for _ in range(LOG)]
depth = [0] * (N + 1)

stack = [(1, 0)]
order = []
while stack:
    u, p = stack.pop()
    parent[0][u] = p
    depth[u] = depth[p] + 1 if p else 0
    order.append(u)
    for v in adj[u]:
        if v != p:
            stack.append((v, u))

for k in range(1, LOG):
    for u in range(1, N + 1):
        parent[k][u] = parent[k - 1][parent[k - 1][u]]

def lca(u, v):
    if depth[u] < depth[v]:
        u, v = v, u
    diff = depth[u] - depth[v]
    k = 0
    while diff:
        if diff & 1:
            u = parent[k][u]
        diff >>= 1
        k += 1
    if u == v:
        return u
    for k in range(LOG - 1, -1, -1):
        if parent[k][u] != parent[k][v]:
            u = parent[k][u]
            v = parent[k][v]
    return parent[0][u]

ans = 0
for v in range(1, N // 2 + 1):
    u, w = pairs[v]
    l = lca(u, w)
    ans += depth[u] + depth[w] - 2 * depth[l]
print(ans)
