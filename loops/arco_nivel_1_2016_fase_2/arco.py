import sys
import bisect

data = sys.stdin.buffer.read().split()
n = int(data[0])
dists = []
for i in range(n):
    x = int(data[1 + 2 * i])
    y = int(data[1 + 2 * i + 1])
    dists.append(x * x + y * y)

sorted_dists = sorted(set(dists))
bit = [0] * (len(sorted_dists) + 1)

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

total = 0
for d in dists:
    idx = bisect.bisect_left(sorted_dists, d)
    total += bit_sum(idx)
    bit_add(idx, 1)

print(total)
