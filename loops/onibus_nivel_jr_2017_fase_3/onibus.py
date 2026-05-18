import sys
from collections import deque

def solve():
    data = sys.stdin.read().split()
    n = int(data[0]); a = int(data[1]); b = int(data[2])
    adj = [[] for _ in range(n + 1)]
    for i in range(n - 1):
        p = int(data[3 + 2*i]); q = int(data[4 + 2*i])
        adj[p].append(q); adj[q].append(p)
    dist = [-1] * (n + 1)
    q = deque([a])
    dist[a] = 0
    while q:
        u = q.popleft()
        if u == b:
            print(dist[u])
            return
        for v in adj[u]:
            if dist[v] == -1:
                dist[v] = dist[u] + 1
                q.append(v)

if __name__ == '__main__':
    solve()
