import sys

data = sys.stdin.buffer.read().split()
it = iter(data)
n = int(next(it))
q = int(next(it))
a = [0] + [int(next(it)) for _ in range(n)]
bit = [0] * (n + 1)

def bit_add(i, v):
    while i <= n:
        bit[i] += v
        i += i & -i

def bit_sum(i):
    s = 0
    while i > 0:
        s += bit[i]
        i -= i & -i
    return s

for i in range(1, n + 1):
    bit_add(i, a[i])

out = []
for _ in range(q):
    t = int(next(it))
    if t == 0:
        k = int(next(it))
        p = int(next(it))
        diff = p - a[k]
        a[k] = p
        if diff:
            bit_add(k, diff)
    else:
        k = int(next(it))
        out.append(str(bit_sum(k)))

sys.stdout.write('\n'.join(out))
