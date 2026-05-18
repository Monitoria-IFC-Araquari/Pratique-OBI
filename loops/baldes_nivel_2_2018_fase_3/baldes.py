import sys

data = sys.stdin.buffer.read().split()
it = iter(data)
N = int(next(it))
M = int(next(it))
pesos = [int(next(it)) for _ in range(N)]

INF = 10**9
MINF = -10**9

class Node:
    __slots__ = ('min1', 'min2', 'max1', 'max2')
    def __init__(self, min1=INF, min2=INF, max1=MINF, max2=MINF):
        self.min1 = min1
        self.min2 = min2
        self.max1 = max1
        self.max2 = max2

size = 1
while size < N:
    size <<= 1
seg = [Node() for _ in range(2 * size)]

for i in range(N):
    v = pesos[i]
    seg[size + i] = Node(v, INF, v, MINF)
for i in range(size - 1, 0, -1):
    left = seg[2 * i]
    right = seg[2 * i + 1]
    vals_min = sorted([left.min1, left.min2, right.min1, right.min2])
    vals_max = sorted([left.max1, left.max2, right.max1, right.max2], reverse=True)
    seg[i] = Node(vals_min[0], vals_min[1], vals_max[0], vals_max[1])

def update(pos, v):
    idx = size + pos - 1
    seg[idx] = Node(v, INF, v, MINF)
    idx //= 2
    while idx:
        left = seg[2 * idx]
        right = seg[2 * idx + 1]
        vals_min = sorted([left.min1, left.min2, right.min1, right.min2])
        vals_max = sorted([left.max1, left.max2, right.max1, right.max2], reverse=True)
        seg[idx].min1, seg[idx].min2 = vals_min[0], vals_min[1]
        seg[idx].max1, seg[idx].max2 = vals_max[0], vals_max[1]
        idx //= 2

def query(l, r):
    l += size - 1
    r += size - 1
    left_res = Node()
    right_res = Node()
    while l <= r:
        if l & 1:
            vals_min = sorted([left_res.min1, left_res.min2, seg[l].min1, seg[l].min2])
            vals_max = sorted([left_res.max1, left_res.max2, seg[l].max1, seg[l].max2], reverse=True)
            left_res = Node(vals_min[0], vals_min[1], vals_max[0], vals_max[1])
            l += 1
        if not (r & 1):
            vals_min = sorted([right_res.min1, right_res.min2, seg[r].min1, seg[r].min2])
            vals_max = sorted([right_res.max1, right_res.max2, seg[r].max1, seg[r].max2], reverse=True)
            right_res = Node(vals_min[0], vals_min[1], vals_max[0], vals_max[1])
            r -= 1
        l //= 2
        r //= 2
    vals_min = sorted([left_res.min1, left_res.min2, right_res.min1, right_res.min2])
    vals_max = sorted([left_res.max1, left_res.max2, right_res.max1, right_res.max2], reverse=True)
    combined = Node(vals_min[0], vals_min[1], vals_max[0], vals_max[1])
    return combined

out_lines = []
for _ in range(M):
    t = int(next(it))
    if t == 1:
        p = int(next(it))
        i = int(next(it))
        update(i, p)
    else:
        a = int(next(it))
        b = int(next(it))
        res = query(a, b)
        mp = res.min1
        if res.min2 == mp:
            mp2 = INF
        else:
            mp2 = res.min2
        mv = res.max1
        if res.max2 == mv:
            mv2 = MINF
        else:
            mv2 = res.max2
        ans = mv - mp
        if ans < mv - mp2:
            ans = mv - mp2
        if ans < mv2 - mp:
            ans = mv2 - mp
        out_lines.append(str(ans))

sys.stdout.write('\n'.join(out_lines))
