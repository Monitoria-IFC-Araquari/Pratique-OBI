def solve():
    N, E = map(int, input().split())
    dancers = []
    start_set = set()
    for _ in range(E):
        V, D = map(int, input().split())
        dancers.append([V-1, D])
        start_set.add(V-1)
    t = 0
    while True:
        t += 1
        nxt = [(dancers[i][0] + dancers[i][1]) % N for i in range(E)]
        col_same = set()
        for i in range(E):
            for j in range(i+1, E):
                if nxt[i] == nxt[j]:
                    col_same.add(i); col_same.add(j)
        col_adj = set()
        for i in range(E):
            if i in col_same:
                continue
            p, d = dancers[i]
            for j in range(E):
                if j == i or j in col_same:
                    continue
                q, e = dancers[j]
                if d == 1 and e == -1 and (p + 1) % N == q:
                    col_adj.add(i); col_adj.add(j)
                elif d == -1 and e == 1 and (q + 1) % N == p:
                    col_adj.add(i); col_adj.add(j)
        for i in col_same:
            dancers[i][0] = nxt[i]
            dancers[i][1] = -dancers[i][1]
        for i in col_adj:
            dancers[i][1] = -dancers[i][1]
        for i in range(E):
            if i not in col_same and i not in col_adj:
                dancers[i][0] = nxt[i]
        cur_set = set(p for p, _ in dancers)
        if cur_set == start_set:
            print(t)
            return
solve()