from array import array

class Fenwick:
    def __init__(self, n):
        self.n = n
        self.bit = array('i', [0]) * (n + 2)
    def add(self, i, delta):
        i += 1
        n = self.n + 1
        bit = self.bit
        while i <= n:
            bit[i] += delta
            i += i & -i
    def sum(self, i):
        i += 1
        s = 0
        bit = self.bit
        while i > 0:
            s += bit[i]
            i -= i & -i
        return s
    def range_sum(self, l, r):
        if l > r:
            return 0
        return self.sum(r) - self.sum(l - 1)

n, q = map(int, input().split())

row_val = [0] * (n + 1)
row_time = [-1] * (n + 1)
col_val = [0] * (n + 1)
col_time = [-1] * (n + 1)

MAXV = 50
ft_row = [Fenwick(q + 2) for _ in range(MAXV + 1)]
ft_col = [Fenwick(q + 2) for _ in range(MAXV + 1)]

cur_time = -1
out = []
for _ in range(q):
    parts = list(map(int, input().split()))
    t = parts[0]
    cur_time += 1
    if t == 1:
        x, r = parts[1], parts[2]
        old_r = row_val[x]
        old_t = row_time[x]
        if old_t >= 0:
            ft_row[old_r].add(old_t, -1)
        row_val[x] = r
        row_time[x] = cur_time
        ft_row[r].add(cur_time, 1)
    elif t == 2:
        x, r = parts[1], parts[2]
        old_r = col_val[x]
        old_t = col_time[x]
        if old_t >= 0:
            ft_col[old_r].add(old_t, -1)
        col_val[x] = r
        col_time[x] = cur_time
        ft_col[r].add(cur_time, 1)
    elif t == 3:
        x = parts[1]
        tr = row_time[x]
        vr = row_val[x]
        best_freq = -1
        best_val = -1
        other = 0
        for k in range(MAXV + 1):
            cnt = ft_col[k].range_sum(tr + 1, cur_time)
            other += cnt
            if cnt > best_freq or (cnt == best_freq and k > best_val):
                best_freq = cnt
                best_val = k
        cnt_vr = n - other
        if cnt_vr > best_freq or (cnt_vr == best_freq and vr > best_val):
            best_val = vr
        out.append(str(best_val))
    else:
        x = parts[1]
        tc = col_time[x]
        vc = col_val[x]
        best_freq = -1
        best_val = -1
        other = 0
        for k in range(MAXV + 1):
            cnt = ft_row[k].range_sum(tc + 1, cur_time)
            other += cnt
            if cnt > best_freq or (cnt == best_freq and k > best_val):
                best_freq = cnt
                best_val = k
        cnt_vc = n - other
        if cnt_vc > best_freq or (cnt_vc == best_freq and vc > best_val):
            best_val = vc
        out.append(str(best_val))

print('\n'.join(out))
