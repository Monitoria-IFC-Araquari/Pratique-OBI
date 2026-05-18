import sys
import bisect

data = sys.stdin.buffer.read().split()
n = int(data[0])
pts = []
for i in range(n):
    x = int(data[1 + 2 * i])
    y = int(data[1 + 2 * i + 1])
    pts.append((x, y))

real_dists = []
p_prev = 0
for x, y in pts:
    xr = x + p_prev
    yr = y + p_prev
    real_dists.append(xr * xr + yr * yr)

all_dists = sorted(set(real_dists))
bit = [0] * (len(all_dists) + 2)
out_lines = []

def bit_add(i, v):
    i += 1
    while i < len(bit):
        bit[i] += v
        i += i & -i

def bit_sum(i):
    s = 0
    i += 1
    while i > 0:
        s += bit[i]
        i -= i & -i
    return s

out = []
for d in real_dists:
    idx = bisect.bisect_left(all_dists, d)
    pk = bit_sum(idx)
    out.append(str(pk))
    bit_add(idx, 1)

sys.stdout.write('\n'.join(out))
