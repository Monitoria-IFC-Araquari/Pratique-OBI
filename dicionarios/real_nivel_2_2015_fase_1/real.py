N, M = map(int, input().split())
parents = list(map(int, input().split()))
participants = list(map(int, input().split()))
present = [False] * (N + 2)
for p in participants:
    present[p] = True
children = [[] for _ in range(N + 2)]
for i, p in enumerate(parents):
    child = i + 2
    children[p].append(child)
gen_count = {}
gen_present = {}
def dfs(u, gen):
    gen_count[gen] = gen_count.get(gen, 0) + 1
    if u <= N + 1 and present[u]:
        gen_present[gen] = gen_present.get(gen, 0) + 1
    for v in children[u]:
        dfs(v, gen + 1)
dfs(1, 0)
max_gen = max(gen_count.keys())
res = []
for g in range(1, max_gen + 1):
    total = gen_count.get(g, 0)
    pres = gen_present.get(g, 0)
    pct = (pres / total) * 100 if total > 0 else 0.0
    res.append(f"{pct:.2f}")
print(' '.join(res))
