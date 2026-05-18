l, c = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(l)]

orig_row = [[0] * c for _ in range(l)]
orig_col = [[0] * c for _ in range(l)]
for i in range(l):
    for j in range(c):
        v = grid[i][j] - 1
        orig_row[i][j] = v // c
        orig_col[i][j] = v % c

pi_r = [0] * l
ok = True
for i in range(l):
    r = orig_row[i][0]
    for j in range(c):
        if orig_row[i][j] != r:
            ok = False
            break
    pi_r[i] = r
    if not ok:
        break

pi_c = [0] * c
for j in range(c):
    col = orig_col[0][j]
    for i in range(l):
        if orig_col[i][j] != col:
            ok = False
            break
    pi_c[j] = col
    if not ok:
        break

if not ok:
    print(0)
else:
    swaps = []
    pi_r = [x + 1 for x in pi_r]
    pi_c = [x + 1 for x in pi_c]

    visited = [False] * (l + 1)
    for i in range(1, l + 1):
        if not visited[i]:
            cur = i
            cycle = []
            while not visited[cur]:
                visited[cur] = True
                cycle.append(cur)
                cur = pi_r[cur - 1]
            for k in range(1, len(cycle)):
                swaps.append(f'L {cycle[0]} {cycle[k]}')

    visited = [False] * (c + 1)
    for i in range(1, c + 1):
        if not visited[i]:
            cur = i
            cycle = []
            while not visited[cur]:
                visited[cur] = True
                cycle.append(cur)
                cur = pi_c[cur - 1]
            for k in range(1, len(cycle)):
                swaps.append(f'C {cycle[0]} {cycle[k]}')

    print(len(swaps))
    for s in swaps:
        print(s)
