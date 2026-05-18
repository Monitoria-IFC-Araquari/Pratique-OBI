import sys

MOD = 1000000007
n = int(sys.stdin.readline())

if n == 0:
    print(1)
elif n == 1:
    print(1)
elif n == 2:
    print(5)
else:
    f0, f1, f2 = 1, 1, 5
    for _ in range(3, n + 1):
        f3 = (f2 + 4 * f1 + 2 * f0) % MOD
        f0, f1, f2 = f1, f2, f3
    print(f2)
