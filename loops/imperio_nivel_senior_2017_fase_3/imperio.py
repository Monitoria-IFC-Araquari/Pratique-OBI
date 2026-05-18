import sys
sys.setrecursionlimit(200000)

n = int(input())
g = [[] for _ in range(n)]
for _ in range(n - 1):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    g[a].append(b)
    g[b].append(a)

vis = [False] * n
sz = [0] * n
ans = n

def dfs(u):
    global ans
    vis[u] = True
    sz[u] = 1
    for v in g[u]:
        if not vis[v]:
            dfs(v)
            sz[u] += sz[v]
            diff = abs(n - 2 * sz[v])
            if diff < ans:
                ans = diff

dfs(0)
print(ans)
