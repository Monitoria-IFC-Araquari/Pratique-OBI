grid = [list(map(int, input().split())) for _ in range(3)]
zeros = [(i, j) for i in range(3) for j in range(3) if grid[i][j] == 0]
target = 0
for row in grid:
    if all(x != 0 for x in row):
        target = sum(row)
        break
if target == 0:
    for j in range(3):
        col = [grid[i][j] for i in range(3)]
        if all(x != 0 for x in col):
            target = sum(col)
            break
if target == 0:
    diag = [grid[i][i] for i in range(3)]
    if all(x != 0 for x in diag):
        target = sum(diag)
if target == 0:
    diag = [grid[i][2 - i] for i in range(3)]
    if all(x != 0 for x in diag):
        target = sum(diag)
if target == 0:
    for row in grid:
        s = sum(x for x in row if x != 0)
        z = row.count(0)
        if z == 1:
            target = s
            break
    if target == 0:
        for j in range(3):
            col = [grid[i][j] for i in range(3)]
            s = sum(x for x in col if x != 0)
            z = col.count(0)
            if z == 1:
                target = s
                break

while zeros:
    changed = False
    for i, j in zeros[:]:
        row = grid[i]
        col = [grid[r][j] for r in range(3)]
        if row.count(0) == 1 and sum(row) < target:
            grid[i][j] = target - sum(row)
            zeros.remove((i, j))
            changed = True
        elif col.count(0) == 1 and sum(col) < target:
            grid[i][j] = target - sum(col)
            zeros.remove((i, j))
            changed = True
    if not changed:
        for i, j in zeros[:]:
            grid[i][j] = target - sum(grid[i])
            zeros.remove((i, j))
            break

for row in grid:
    print(' '.join(map(str, row)))
