import sys
sys.setrecursionlimit(10**6)

def solve():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    E = int(next(it))
    R = int(next(it))

    adj = [[] for _ in range(E + 1)]
    for _ in range(R):
        a = int(next(it)); b = int(next(it)); c = int(next(it))
        adj[a].append((b, c))
        adj[b].append((a, c))

    visited = [0] * (E + 1)
    parent = [0] * (E + 1)
    depth = [0] * (E + 1)
    edge_to_parent = [0] * (E + 1)
    cycle_id = [-1] * (E + 1)
    cycle_len = []
    in_cycle = [False] * (E + 1)

    def dfs(u, p, d):
        visited[u] = 1
        parent[u] = p
        depth[u] = d
        for v, w in adj[u]:
            if v == p:
                continue
            if not visited[v]:
                edge_to_parent[v] = w
                dfs(v, u, d + 1)
            elif visited[v] == 1 and depth[v] < depth[u]:
                nodes = []
                total = w
                cur = u
                while cur != v:
                    total += edge_to_parent[cur]
                    nodes.append(cur)
                    cur = parent[cur]
                nodes.append(v)
                cid = len(cycle_len)
                cycle_len.append(total)
                for x in nodes:
                    cycle_id[x] = cid
                    in_cycle[x] = True
        visited[u] = 2

    for i in range(1, E + 1):
        if not visited[i]:
            dfs(i, 0, 0)

    dist_to_cycle = [0] * (E + 1)
    for i in range(1, E + 1):
        if not in_cycle[i]:
            best = 10**18
            stack = [(i, 0)]
            seen = {i}
            while stack:
                u, d = stack.pop()
                if in_cycle[u]:
                    best = min(best, d)
                    continue
                for v, w in adj[u]:
                    if v not in seen:
                        seen.add(v)
                        stack.append((v, d + w))
            dist_to_cycle[i] = best if best != 10**18 else -1

    reachable_cycles = [[] for _ in range(E + 1)]
    for i in range(1, E + 1):
        if in_cycle[i]:
            reachable_cycles[i].append((cycle_id[i], 0))
        elif dist_to_cycle[i] >= 0:
            seen = {i}
            stack = [(i, 0)]
            found = set()
            while stack:
                u, d = stack.pop()
                if in_cycle[u]:
                    cid = cycle_id[u]
                    if cid not in found:
                        found.add(cid)
                        reachable_cycles[i].append((cid, d))
                    continue
                for v, w in adj[u]:
                    if v not in seen:
                        seen.add(v)
                        stack.append((v, d + w))

    K = int(next(it))
    out_lines = []
    for _ in range(K):
        X = int(next(it))
        T = int(next(it))
        best = 10**18
        for cid, d in reachable_cycles[X]:
            total = 2 * d + cycle_len[cid]
            if total >= T:
                best = min(best, total)
        out_lines.append(str(best if best != 10**18 else -1))
    sys.stdout.write("\n".join(out_lines))

if __name__ == "__main__":
    solve()
