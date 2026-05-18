import sys
import bisect

data = sys.stdin.buffer.read().split()
it = iter(data)
C = int(next(it))
T = int(next(it))
raios = [int(next(it)) for _ in range(C)]
raios2 = [r * r for r in raios]
total = 0
for _ in range(T):
    x = int(next(it))
    y = int(next(it))
    d2 = x * x + y * y
    total += C - bisect.bisect_left(raios2, d2)
print(total)
