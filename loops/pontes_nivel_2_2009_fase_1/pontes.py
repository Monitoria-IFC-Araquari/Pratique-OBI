import sys
import heapq

def solve():
    data = sys.stdin.read().split()
    N, M = int(data[0]), int(data[1])
    adj = [[] for _ in range(N + 2)]
    idx = 2
    for _ in range(M):
        S, T, B = int(data[idx]), int(data[idx+1]), int(data[idx+2])
        idx += 3
        adj[S].append((T, B))
        adj[T].append((S, B))
    INF = 10 ** 9
    dist = [INF] * (N + 2)
    dist[0] = 0
    pq = [(0, 0)]
    while pq:
        d, u = heapq.heappop(pq)
        if d != dist[u]:
            continue
        for v, w in adj[u]:
            nd = d + w
            if nd < dist[v]:
                dist[v] = nd
                heapq.heappush(pq, (nd, v))
    print(dist[N + 1])

if __name__ == '__main__':
    solve()
