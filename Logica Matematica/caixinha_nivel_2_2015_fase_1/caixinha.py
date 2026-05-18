n, m = map(int, input().split())

def C2(x):
    return x * (x - 1) // 2 if x >= 2 else 0

total = C2(n - 1)
total -= 3 * C2(n - m - 1)
total += 3 * C2(n - 2 * m - 1)
total -= C2(n - 3 * m - 1)
print(total)
