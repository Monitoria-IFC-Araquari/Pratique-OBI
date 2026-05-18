class BIT:
    def __init__(self, n):
        self.n = n
        self.bit = [0] * (n + 1)
    def add(self, i, v):
        i += 1
        while i <= self.n:
            self.bit[i] += v
            i += i & -i
    def sum(self, i):
        i += 1
        s = 0
        while i > 0:
            s += self.bit[i]
            i -= i & -i
        return s

n = int(input())
deck = list(map(int, input().split()))

pos = [0] * (n + 1)
for i, c in enumerate(deck):
    pos[c] = i

bit = BIT(n)
for i in range(n):
    bit.add(i, 1)

rounds = 1
prev = -1
for i in range(1, n + 1):
    cur = bit.sum(pos[i])
    if cur < prev:
        rounds += 1
    prev = cur
    bit.add(pos[i], -1)

print(rounds)
