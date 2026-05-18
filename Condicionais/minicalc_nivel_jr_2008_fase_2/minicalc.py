import math

n, d, q = map(int, input().split())
g = math.gcd(d, q)
d //= g
q //= g

lim = 2 * n
if d < lim and q < lim:
    print(d, q)
else:
    print("IMPOSSIVEL")
