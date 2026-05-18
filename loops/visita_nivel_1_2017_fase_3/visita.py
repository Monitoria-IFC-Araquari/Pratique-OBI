def solve():
    import sys
    sys.setrecursionlimit(20000)
    data = list(map(int, sys.stdin.read().split()))
    n, a, b = data[0], data[1], data[2]
    adj = [[] for _ in range(n + 1)]
    idx = 3
    for _ in range(n - 1):
        p, q, d = data[idx], data[idx+1], data[idx+2]
        idx += 3
        adj[p].append((q, d))
        adj[q].append((p, d))
    parent = [0] * (n + 1)
    dist = [0] * (n + 1)
    stack = [a]
    parent[a] = -1
    while stack:
        u = stack.pop()
        for v, w in adj[u]:
            if v != parent[u]:
                parent[v] = u
                dist[v] = dist[u] + w
                stack.append(v)
    print(dist[b])

if __name__ == '__main__':
    solve()
