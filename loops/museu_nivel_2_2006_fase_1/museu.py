import sys
import heapq

def solve():
    data = sys.stdin.read().split()
    if not data:
        return
    it = iter(data)
    S = int(next(it))
    C = int(next(it))
    room_time = [0] + [int(next(it)) for _ in range(S)]
    adj = [[] for _ in range(S + 1)]
    for _ in range(C):
        i = int(next(it))
        f = int(next(it))
        t = int(next(it))
        adj[i].append((f, t))

    INF = 10**15
    ans = INF

    for src in range(1, S + 1):
        dist = [INF] * (S + 1)
        dist[src] = 0
        pq = [(0, src)]
        while pq:
            d, u = heapq.heappop(pq)
            if d != dist[u]:
                continue
            for v, w in adj[u]:
                nd = d + w + room_time[v]
                if nd < dist[v]:
                    dist[v] = nd
                    heapq.heappush(pq, (nd, v))
        if dist[src] != 0:
            ans = min(ans, dist[src] + room_time[src])

    print(ans)

if __name__ == "__main__":
    solve()
