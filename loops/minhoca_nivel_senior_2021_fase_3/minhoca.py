import sys
sys.setrecursionlimit(100010)

n = int(input())
adj = [[] for _ in range(n + 1)]
for _ in range(n - 1):
    x, y = map(int, input().split())
    adj[x].append(y)
    adj[y].append(x)

def bfs(start):
    dist = [-1] * (n + 1)
    dist[start] = 0
    q = [start]
    for u in q:
        for v in adj[u]:
            if dist[v] == -1:
                dist[v] = dist[u] + 1
                q.append(v)
    far = max(range(1, n + 1), key=lambda x: dist[x])
    return far, dist

a, _ = bfs(1)
b, da = bfs(a)
_, db = bfs(b)
diam = da[b]

if diam % 2 == 0:
    k = diam // 2
    center = next(v for v in range(1, n + 1) if da[v] == k and db[v] == k)
    total = 0
    pairs = 0
    for nb in adj[center]:
        cnt = 0
        stack = [(nb, center, 1)]
        while stack:
            u, p, d = stack.pop()
            if d == k:
                cnt += 1
            if d < k:
                for v in adj[u]:
                    if v != p:
                        stack.append((v, u, d + 1))
        pairs += total * cnt
        total += cnt
    print(diam + 1)
    print(pairs)
else:
    k = diam // 2
    c1 = next(v for v in range(1, n + 1) if da[v] == k and db[v] == k + 1)
    c2 = next(v for v in range(1, n + 1) if da[v] == k + 1 and db[v] == k)
    cnt1 = 0
    stack = [(c1, c2, 0)]
    while stack:
        u, p, d = stack.pop()
        if d == k and u != c1:
            cnt1 += 1
        if d < k:
            for v in adj[u]:
                if v != p:
                    stack.append((v, u, d + 1))
    cnt2 = 0
    stack = [(c2, c1, 0)]
    while stack:
        u, p, d = stack.pop()
        if d == k and u != c2:
            cnt2 += 1
        if d < k:
            for v in adj[u]:
                if v != p:
                    stack.append((v, u, d + 1))
    print(diam + 1)
    print(cnt1 * cnt2)
