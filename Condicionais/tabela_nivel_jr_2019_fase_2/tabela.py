j, p, v, e, d = list(map(int, input().split()))

if j == -1:
    j = v + e + d
if p == -1:
    p = 3 * v + e
if v == -1:
    v = (p - e) // 3
if e == -1:
    e = p - 3 * v
if d == -1:
    d = j - v - e

print(j, p, v, e, d)
