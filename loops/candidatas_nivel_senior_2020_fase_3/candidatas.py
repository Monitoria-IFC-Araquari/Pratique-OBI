import sys
import math
sys.setrecursionlimit(10**6)

n, m = map(int, input().split())
s = list(map(int, input().split()))

size = 1
while size < n:
    size <<= 1

class Node:
    __slots__ = ('gcd', 'cnt', 'pref', 'suff')
    def __init__(self):
        self.gcd = 0
        self.cnt = 0
        self.pref = []
        self.suff = []

def merge(a, b):
    if a.gcd == 0:
        return b
    if b.gcd == 0:
        return a
    res = Node()
    res.gcd = math.gcd(a.gcd, b.gcd)
    res.pref = list(a.pref)
    for g, c in b.pref:
        ng = math.gcd(a.gcd, g)
        if res.pref and res.pref[-1][0] == ng:
            res.pref[-1] = (ng, res.pref[-1][1] + c)
        else:
            res.pref.append((ng, c))
    res.suff = list(b.suff)
    for g, c in a.suff:
        ng = math.gcd(b.gcd, g)
        if res.suff and res.suff[-1][0] == ng:
            res.suff[-1] = (ng, res.suff[-1][1] + c)
        else:
            res.suff.append((ng, c))
    cross = 0
    for g1, c1 in a.suff:
        for g2, c2 in b.pref:
            if math.gcd(g1, g2) > 1:
                cross += c1 * c2
    res.cnt = a.cnt + b.cnt + cross
    return res

def make_node(v):
    node = Node()
    node.gcd = v
    if v > 1:
        node.cnt = 1
    node.pref = [(v, 1)]
    node.suff = [(v, 1)]
    return node

tree = [Node() for _ in range(2 * size)]
for i in range(n):
    tree[size + i] = make_node(s[i])
for i in range(size - 1, 0, -1):
    tree[i] = merge(tree[2 * i], tree[2 * i + 1])

def update(pos, val):
    p = size + pos
    tree[p] = make_node(val)
    p //= 2
    while p:
        tree[p] = merge(tree[2 * p], tree[2 * p + 1])
        p //= 2

def query(l, r):
    l += size
    r += size
    left_res = Node()
    right_res = Node()
    while l <= r:
        if l % 2 == 1:
            left_res = merge(left_res, tree[l])
            l += 1
        if r % 2 == 0:
            right_res = merge(tree[r], right_res)
            r -= 1
        l //= 2
        r //= 2
    return merge(left_res, right_res)

out_lines = []
for _ in range(m):
    parts = list(map(int, input().split()))
    t = parts[0]
    if t == 1:
        i, v = parts[1], parts[2]
        update(i - 1, v)
    else:
        e, d = parts[1], parts[2]
        node = query(e - 1, d - 1)
        out_lines.append(str(node.cnt))

sys.stdout.write('\n'.join(out_lines))
