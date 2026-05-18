C, N = map(int, input().split())
installed = {}
for _ in range(C):
    p, v = map(int, input().split())
    installed[p] = max(installed.get(p, 0), v)
updates = {}
for _ in range(N):
    p, v = map(int, input().split())
    if p in updates:
        updates[p] = max(updates[p], v)
    else:
        updates[p] = v
res = []
for p, v in sorted(updates.items()):
    if v > installed.get(p, 0):
        res.append(f"{p} {v}")
print('\n'.join(res))
