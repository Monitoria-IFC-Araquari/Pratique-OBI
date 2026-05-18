n = int(input())
p = list(map(int, input().split()))

bit = [0] * (n + 2)

def add(i, v):
    i += 1
    while i <= n:
        bit[i] += v
        i += i & -i

def sum_(i):
    i += 1
    s = 0
    while i > 0:
        s += bit[i]
        i -= i & -i
    return s

inv = 0
for i, x in enumerate(p):
    inv += i - sum_(x)
    add(x, 1)

print(inv)
