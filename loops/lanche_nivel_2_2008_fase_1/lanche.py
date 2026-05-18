s, c = map(int, input().split())
INF = 10 ** 9
dist = [[INF] * s for _ in range(s)]
for i in range(s):
    dist[i][i] = 0
for _ in range(c):
    a, b, d = map(int, input().split())
    a -= 1
    b -= 1
    dist[a][b] = d
    dist[b][a] = d
for k in range(s):
    dk = dist[k]
    for i in range(s):
        di = dist[i]
        dik = di[k]
        if dik == INF:
            continue
        for j in range(s):
            nd = dik + dk[j]
            if nd < di[j]:
                di[j] = nd
best = INF
for i in range(s):
    worst = 0
    for j in range(s):
        if dist[i][j] > worst:
            worst = dist[i][j]
    if worst < best:
        best = worst
print(best)
