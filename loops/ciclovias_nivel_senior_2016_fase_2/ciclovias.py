import sys
sys.setrecursionlimit(10**6)

n, m = map(int, input().split())
adj = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    adj[a].append(b)
    adj[b].append(a)

for v in range(1, n + 1):
    adj[v].sort()

from functools import lru_cache

@lru_cache(None)
def odd(v, last_even):
    best = 1
    for u in adj[v]:
        best = max(best, 1 + even(u, v))
    return best

@lru_cache(None)
def even(v, last_odd):
    best = 1
    for w in adj[v]:
        if w > last_odd:
            best = max(best, 1 + odd(w, v))
    return best

res = [0] * (n + 1)
for v in range(1, n + 1):
    res[v] = odd(v, 0)
print(' '.join(map(str, res[1:])))
