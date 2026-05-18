N, M = map(int, input().split())
bad = [0] * N
for _ in range(M):
    a, b = map(int, input().split())
    bad[a - 1] |= 1 << (b - 1)
    bad[b - 1] |= 1 << (a - 1)
ans = 0
for mask in range(1 << N):
    ok = True
    for i in range(N):
        if mask & (1 << i):
            if mask & bad[i]:
                ok = False
                break
    if ok:
        ans += 1
print(ans - 1)
