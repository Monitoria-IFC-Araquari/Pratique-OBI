N, D = map(int, input().split())
pts = [tuple(map(int, input().split())) for _ in range(N)]
vis = [False] * N
vis[0] = True
stack = [0]
while stack:
    u = stack.pop()
    x1, y1 = pts[u]
    for v in range(N):
        if not vis[v]:
            x2, y2 = pts[v]
            if (x1 - x2) ** 2 + (y1 - y2) ** 2 <= D * D:
                vis[v] = True
                stack.append(v)
print('S' if all(vis) else 'N')
