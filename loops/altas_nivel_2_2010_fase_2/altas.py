N, K = map(int, input().split())

def soma_binomios(t, k):
    s = 0
    c = 1
    for i in range(1, k + 1):
        c = c * (t - i + 1) // i
        s += c
        if s >= N:
            return s
    return s

lo, hi = 1, N
while lo < hi:
    mid = (lo + hi) // 2
    if soma_binomios(mid, K) >= N:
        hi = mid
    else:
        lo = mid + 1
print(lo)
