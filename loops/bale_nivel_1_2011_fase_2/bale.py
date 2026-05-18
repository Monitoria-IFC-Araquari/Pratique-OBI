import sys

n = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))
max_val = max(a)
bit = [0] * (max_val + 2)

def bit_add(i, v):
    while i <= max_val:
        bit[i] += v
        i += i & -i

def bit_sum(i):
    s = 0
    while i > 0:
        s += bit[i]
        i -= i & -i
    return s

total = 0
for val in a:
    total += bit_sum(max_val) - bit_sum(val)
    bit_add(val, 1)

print(total)
