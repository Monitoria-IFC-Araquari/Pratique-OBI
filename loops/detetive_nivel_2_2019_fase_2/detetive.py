def solve():
    N, M, K = map(int, input().split())
    skills = list(map(int, input().split()))
    adj = [[] for _ in range(N)]
    for _ in range(M):
        a, b = map(int, input().split())
        adj[a].append(b)
        adj[b].append(a)
    visited = [False]*N
    from collections import deque
    q = deque([K])
    visited[K] = True
    count = 0
    while q:
        v = q.popleft()
        for u in adj[v]:
            if not visited[u] and skills[u] <= skills[K]:
                visited[u] = True
                q.append(u)
                count += 1
    print(count)
solve()