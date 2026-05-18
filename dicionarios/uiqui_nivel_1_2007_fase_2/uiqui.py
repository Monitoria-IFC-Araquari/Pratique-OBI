def solve():
    import sys
    from collections import deque
    data = sys.stdin.read().splitlines()
    n = int(data[0].strip())
    graph = {}
    all_pages = set()
    for i in range(1, n + 1):
        x, y = data[i].strip().split()
        graph.setdefault(x, []).append(y)
        all_pages.add(x)
        all_pages.add(y)
    pages = sorted(all_pages)
    idx_map = {p: i for i, p in enumerate(pages)}
    size = len(pages)
    adj = [[] for _ in range(size)]
    for x in graph:
        for y in graph[x]:
            adj[idx_map[x]].append(idx_map[y])
    for i in range(size - 1):
        adj[i].append(i + 1)
        adj[i + 1].append(i)
    paulo, andre = data[n + 1].strip().split()
    s = idx_map[paulo]
    t = idx_map[andre]
    dist = [-1] * size
    dist[s] = 0
    q = deque([s])
    while q:
        u = q.popleft()
        if u == t:
            print(dist[u])
            return
        for v in adj[u]:
            if dist[v] == -1:
                dist[v] = dist[u] + 1
                q.append(v)

if __name__ == '__main__':
    solve()
