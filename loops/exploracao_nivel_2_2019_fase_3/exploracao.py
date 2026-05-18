def solve():
    N, M = map(int, input().split())
    adj = [[] for _ in range(N)]
    edges = []
    for _ in range(M):
        a, b = map(int, input().split())
        adj[a].append(b)
        adj[b].append(a)
        edges.append((a, b))
    visited = [False]*N
    low = [0]*N
    tin = [0]*N
    timer = 0
    critical = set()
    def dfs(v, p):
        nonlocal timer
        visited[v] = True
        tin[v] = low[v] = timer
        timer += 1
        for u in adj[v]:
            if u == p:
                continue
            if visited[u]:
                low[v] = min(low[v], tin[u])
            else:
                dfs(u, v)
                low[v] = min(low[v], low[u])
                if low[u] > tin[v]:
                    critical.add((min(v,u), max(v,u)))
    for i in range(N):
        if not visited[i]:
            dfs(i, -1)
    print(len(critical))
solve()