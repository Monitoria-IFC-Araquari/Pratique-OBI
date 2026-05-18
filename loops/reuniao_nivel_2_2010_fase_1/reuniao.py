N, M = map(int, input().split())
INF = 10**9
dist = [[INF] * N for _ in range(N)]
for i in range(N):
    dist[i][i] = 0
for _ in range(M):
    a, b, c = map(int, input().split())
    dist[a][b] = c
    dist[b][a] = c
for k in range(N):
    dk = dist[k]
    for i in range(N):
        dik = dist[i][k]
        if dik == INF:
            continue
        di = dist[i]
        for j in range(N):
            nd = dik + dk[j]
            if nd < di[j]:
                di[j] = nd
ans = INF
for i in range(N):
    ans = min(ans, max(dist[i]))
print(ans)
