def solve():
    import sys
    data = sys.stdin.buffer.read().split()
    it = iter(data)
    N = int(next(it)); M = int(next(it))
    class BIT:
        def __init__(self, n):
            self.n = n
            self.t = [0]*(n+2)
        def add(self, i, v):
            while i <= self.n:
                self.t[i] += v
                i += i & -i
        def range_add(self, l, r, v):
            if l <= r:
                self.add(l, v)
                self.add(r+1, -v)
        def query(self, i):
            s = 0
            while i > 0:
                s += self.t[i]
                i -= i & -i
            return s
    bit_c = BIT(N)
    bit_l = BIT(N)
    for _ in range(M):
        t = int(next(it))
        if t == 3:
            i = int(next(it))
            val = bit_c.query(i) + bit_l.query(i) * i
            sys.stdout.write(str(val) + '\n')
        elif t == 1:
            i = int(next(it)); v = int(next(it))
            end = min(N, i + v - 1)
            bit_c.range_add(i, end, v + i)
            bit_l.range_add(i, end, -1)
        else:
            i = int(next(it)); v = int(next(it))
            start = max(1, i - v + 1)
            bit_c.range_add(start, i, v - i)
            bit_l.range_add(start, i, 1)
solve()