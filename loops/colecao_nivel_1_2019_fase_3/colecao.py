n, m = map(int, input().split())
adj = [[] for _ in range(n + 1)]
for _ in range(m):
    u, v = map(int, input().split())
    adj[u].append(v)
    adj[v].append(u)
incl = [False] * (n + 1)
for i in range(n, 0, -1):
    ok = True
    for v in adj[i]:
        if incl[v]:
            ok = False
            break
    if ok:
        incl[i] = True
ans = [i for i in range(1, n + 1) if incl[i]]
print(len(ans))
print(' '.join(map(str, ans)))
