import sys
sys.setrecursionlimit(100010)

n, m = map(int, input().split())
adj = [[] for _ in range(n + 1)]
for _ in range(m):
    p, q = map(int, input().split())
    adj[p].append(q)
    adj[q].append(p)

central = max(range(1, n + 1), key=lambda x: len(adj[x]))

depth = [-1] * (n + 1)
parent = [-1] * (n + 1)
cycle_len = 0

def dfs(u, p):
    global cycle_len
    depth[u] = depth[p] + 1 if p != -1 else 0
    parent[u] = p
    for v in adj[u]:
        if v == central or v == p:
            continue
        if depth[v] != -1:
            l = depth[u] - depth[v] + 1
            if l > cycle_len:
                cycle_len = l
        elif depth[v] == -1:
            dfs(v, u)

start = 1
while start == central:
    start += 1
dfs(start, -1)

print(cycle_len)
