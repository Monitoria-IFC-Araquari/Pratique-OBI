import sys
from collections import deque

def solve():
    data = sys.stdin.read().split()
    it = iter(data)
    L = int(next(it)); C = int(next(it))
    var_names = set()
    grid = []
    for _ in range(L):
        row = []
        for _ in range(C):
            name = next(it)
            var_names.add(name)
            row.append(name)
        row_sum = int(next(it))
        grid.append((row, row_sum))
    col_sums = [int(next(it)) for _ in range(C)]

    var_to_idx = {v: i for i, v in enumerate(sorted(var_names))}
    V = len(var_to_idx)
    var_val = [None] * V

    row_known = [0] * L
    col_known = [0] * C
    row_cnt = [C] * L
    col_cnt = [L] * C
    row_unknown_sum = [s for _, s in grid]
    col_unknown_sum = col_sums[:]

    var_in_rows = {v: [] for v in var_names}
    var_in_cols = {v: [] for v in var_names}
    for i, (row, _) in enumerate(grid):
        for j, name in enumerate(row):
            var_in_rows[name].append((i, j))
            var_in_cols[name].append((j, i))

    q = deque()
    for i in range(L):
        if row_cnt[i] == 1:
            q.append(('row', i))
    for j in range(C):
        if col_cnt[j] == 1:
            q.append(('col', j))

    while q:
        tp, idx = q.popleft()
        if tp == 'row':
            if row_cnt[idx] != 1:
                continue
            last_val = None
            last_name = None
            for j in range(C):
                name = grid[idx][0][j]
                if var_val[var_to_idx[name]] is None:
                    last_name = name
                    last_val = row_unknown_sum[idx]
                    break
            if last_name is not None:
                var_val[var_to_idx[last_name]] = last_val
                for ri, cj in var_in_rows[last_name]:
                    row_cnt[ri] -= 1
                    row_unknown_sum[ri] -= last_val
                    if row_cnt[ri] == 1:
                        q.append(('row', ri))
                for cj, ri in var_in_cols[last_name]:
                    col_cnt[cj] -= 1
                    col_unknown_sum[cj] -= last_val
                    if col_cnt[cj] == 1:
                        q.append(('col', cj))
        else:
            if col_cnt[idx] != 1:
                continue
            last_val = None
            last_name = None
            for i in range(L):
                name = grid[i][0][idx]
                if var_val[var_to_idx[name]] is None:
                    last_name = name
                    last_val = col_unknown_sum[idx]
                    break
            if last_name is not None:
                var_val[var_to_idx[last_name]] = last_val
                for ri, cj in var_in_rows[last_name]:
                    row_cnt[ri] -= 1
                    row_unknown_sum[ri] -= last_val
                    if row_cnt[ri] == 1:
                        q.append(('row', ri))
                for cj, ri in var_in_cols[last_name]:
                    col_cnt[cj] -= 1
                    col_unknown_sum[cj] -= last_val
                    if col_cnt[cj] == 1:
                        q.append(('col', cj))

    out = []
    for name in sorted(var_names):
        out.append(f"{name} {var_val[var_to_idx[name]]}")
    sys.stdout.write('\n'.join(out))

if __name__ == '__main__':
    solve()
