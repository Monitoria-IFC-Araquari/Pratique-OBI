def solve():
    import sys
    sys.setrecursionlimit(1000000)
    N, M = map(int, input().split())
    adj = [[] for _ in range(N)]
    for _ in range(M):
        a, b = map(int, input().split())
        adj[a].append(b)
        adj[b].append(a)
    color = [-1]*N
    def dfs(v, c):
        color[v] = c
        for u in adj[v]:
            if color[u] == -1:
                if not dfs(u, 1-c):
                    return False
            elif color[u] == c:
                return False
        return True
    for i in range(N):
        if color[i] == -1:
            if not dfs(i, 0):
                print("NAO")
                return
    print("SIM")
solve()