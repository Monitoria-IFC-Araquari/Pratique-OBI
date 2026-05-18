import sys
sys.setrecursionlimit(1 << 20)

n = int(input())
f = [0] + list(map(int, input().split()))

indeg = [0] * (n + 1)
for i in range(1, n + 1):
    indeg[f[i]] += 1

q = [i for i in range(1, n + 1) if indeg[i] == 0]
for u in q:
    indeg[f[u]] -= 1
    if indeg[f[u]] == 0:
        q.append(f[u])

cycle_nodes = [i for i in range(1, n + 1) if indeg[i] > 0]

pos_in_cycle = {}
cycle_order = []
seen = set()
for start in cycle_nodes:
    if start in seen:
        continue
    cur = start
    while cur not in seen:
        seen.add(cur)
        cycle_order.append(cur)
        pos_in_cycle[cur] = len(cycle_order) - 1
        cur = f[cur]

cycle_len = len(cycle_order)

entry = [0] * (n + 1)
depth = [0] * (n + 1)

for u in cycle_nodes:
    entry[u] = u
    depth[u] = 0

for u in reversed(q):
    v = f[u]
    entry[u] = entry[v]
    depth[u] = depth[v] + 1

qry = int(input())
out_lines = []
for _ in range(qry):
    a, b = map(int, input().split())
    if a == b:
        out_lines.append('0')
        continue
    ca, cb = entry[a], entry[b]
    da, db = depth[a], depth[b]
    if ca == cb:
        out_lines.append(str(abs(da - db)))
    else:
        pa, pb = pos_in_cycle[ca], pos_in_cycle[cb]
        dfwd = (pb - pa + cycle_len) % cycle_len
        t1 = max(da + dfwd, db)
        t2 = max(da, db + cycle_len - dfwd)
        out_lines.append(str(min(t1, t2)))

sys.stdout.write('\n'.join(out_lines))
