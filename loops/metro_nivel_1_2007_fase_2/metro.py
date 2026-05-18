n = int(input())
k = int(input())
paes = list(map(int, input().split()))

lo, hi = 1, max(paes)
ans = 0
while lo <= hi:
    mid = (lo + hi) // 2
    total = sum(p // mid for p in paes)
    if total >= n:
        ans = mid
        lo = mid + 1
    else:
        hi = mid - 1

print(ans)
