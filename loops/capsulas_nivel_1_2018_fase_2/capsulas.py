n, f = map(int, input().split())
c = list(map(int, input().split()))

lo, hi = 0, 10**8
while lo < hi:
    mid = (lo + hi) // 2
    total = 0
    for ci in c:
        total += mid // ci
        if total >= f:
            break
    if total >= f:
        hi = mid
    else:
        lo = mid + 1

print(lo)
