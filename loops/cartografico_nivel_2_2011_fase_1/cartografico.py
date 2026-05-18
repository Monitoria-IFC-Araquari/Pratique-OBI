import sys
sys.setrecursionlimit(1 << 20)

n = int(sys.stdin.readline())
g = [[] for _ in range(n + 1)]
for _ in range(n - 1):
    u, v = map(int, sys.stdin.readline().split())
    g[u].append(v)
    g[v].append(u)

def dfs(u, p):
    far_node, far_dist = u, 0
    stack = [(u, p, 0)]
    while stack:
        u, p, d = stack.pop()
        if d > far_dist:
            far_dist = d
            far_node = u
        for v in g[u]:
            if v != p:
                stack.append((v, u, d + 1))
    return far_node, far_dist

a, _ = dfs(1, 0)
_, ans = dfs(a, 0)
print(ans)
