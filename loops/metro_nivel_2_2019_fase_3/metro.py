import sys
sys.setrecursionlimit(200010)

def find_diameter_and_centers(adj, n):
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
    b, dist_a = bfs(a)
    _, dist_b = bfs(b)
    diam = dist_a[b]
    centers = []
    for v in range(1, n + 1):
        if dist_a[v] + dist_b[v] == diam:
            if max(dist_a[v], dist_b[v]) == (diam + 1) // 2:
                centers.append(v)
    return centers

n, m = map(int, input().split())
adj1 = [[] for _ in range(n + 1)]
for _ in range(n - 1):
    a, b = map(int, input().split())
    adj1[a].append(b)
    adj1[b].append(a)

adj2 = [[] for _ in range(m + 1)]
for _ in range(m - 1):
    x, y = map(int, input().split())
    adj2[x].append(y)
    adj2[y].append(x)

c1 = find_diameter_and_centers(adj1, n)
c2 = find_diameter_and_centers(adj2, m)
print(c1[0], c2[0])
