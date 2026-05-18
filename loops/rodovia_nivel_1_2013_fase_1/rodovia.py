N = int(input())
edges = [[] for _ in range(N)]
for _ in range(N):
    a, b = map(int, input().split())
    edges[a - 1].append(b - 1)
    edges[b - 1].append(a - 1)
vis = [False] * N
stack = [0]
vis[0] = True
while stack:
    u = stack.pop()
    for v in edges[u]:
        if not vis[v]:
            vis[v] = True
            stack.append(v)
print('S' if all(vis) else 'N')
