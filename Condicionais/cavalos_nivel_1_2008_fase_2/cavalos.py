m, n = map(int, input().split())
if m > n:
    m, n = n, m

if m == 1:
    print(n)
elif m == 2:
    print(4 * (n // 4) + min(2, n % 4) * 2)
else:
    print((m * n + 1) // 2)
