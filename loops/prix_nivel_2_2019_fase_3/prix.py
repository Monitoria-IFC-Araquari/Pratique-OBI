import sys
sys.setrecursionlimit(1 << 30)

def solve():
    N, M = map(int, sys.stdin.readline().split())
    edges = []
    for _ in range(M):
        u, l, r = map(int, sys.stdin.readline().split())
        edges.append((u - 1, l - 1, r - 1))

    def has_cycle(k):
        adj = [[] for _ in range(N)]
        for u, l, r in edges[:k]:
            adj[u].append((l, r))
        vis = [0] * N
        nxt = list(range(N + 1))
        def find(x):
            while nxt[x] != x:
                nxt[x] = nxt[nxt[x]]
                x = nxt[x]
            return x
        def dfs(u):
            vis[u] = 1
            for l, r in adj[u]:
                v = find(l)
                while v <= r:
                    if vis[v] == 1:
                        return True
                    if vis[v] == 0 and dfs(v):
                        return True
                    nxt[v] = v + 1
                    v = find(v)
            vis[u] = 2
            return False
        for i in range(N):
            if vis[i] == 0:
                if dfs(i):
                    return True
        return False

    lo, hi = 1, M
    ans = -1
    while lo <= hi:
        mid = (lo + hi) // 2
        if has_cycle(mid):
            ans = mid
            hi = mid - 1
        else:
            lo = mid + 1
    print(ans)

if __name__ == '__main__':
    solve()
