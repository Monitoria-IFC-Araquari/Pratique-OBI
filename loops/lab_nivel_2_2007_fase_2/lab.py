import heapq

n, m = map(int, input().split())
h0 = [list(map(int, input().split())) for _ in range(n)]

INF = 10 ** 9
dist = [[INF] * m for _ in range(n)]
dist[0][0] = 0
pq = [(0, 0, 0)]
dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]

while pq:
    d, i, j = heapq.heappop(pq)
    if d != dist[i][j]:
        continue
    if i == n - 1 and j == m - 1:
        print(d)
        break
    nd = d + 1
    if nd < dist[i][j]:
        dist[i][j] = nd
        heapq.heappush(pq, (nd, i, j))
    for di, dj in dirs:
        ni, nj = i + di, j + dj
        if not (0 <= ni < n and 0 <= nj < m):
            continue
        for w in range(10):
            curr_h = (h0[i][j] + d + w) % 10
            next_h = (h0[ni][nj] + d + w) % 10
            if next_h <= curr_h + 1:
                nd2 = d + w + 1
                if nd2 < dist[ni][nj]:
                    dist[ni][nj] = nd2
                    heapq.heappush(pq, (nd2, ni, nj))
                break
else:
    print(dist[n-1][m-1])
