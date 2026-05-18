N, M = map(int, input().split())
P = list(map(int, input().split()))
ok = True
for i in range(1, N):
    if P[i] - P[i - 1] > M:
        ok = False
        break
if 42195 - P[-1] > M:
    ok = False
print('S' if ok else 'N')
