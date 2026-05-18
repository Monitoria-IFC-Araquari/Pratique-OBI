n = int(input())
m = [list(map(int, input().split())) for _ in range(n)]

s = sum(m[0])
ok = True
for i in range(n):
    if sum(m[i]) != s:
        ok = False
        break
if ok:
    for j in range(n):
        if sum(m[i][j] for i in range(n)) != s:
            ok = False
            break
if ok:
    if sum(m[i][i] for i in range(n)) != s:
        ok = False
if ok:
    if sum(m[i][n - 1 - i] for i in range(n)) != s:
        ok = False
if ok:
    seen = [False] * (n * n + 1)
    for i in range(n):
        for j in range(n):
            v = m[i][j]
            if v < 1 or v > n * n or seen[v]:
                ok = False
                break
            seen[v] = True
        if not ok:
            break

print(s if ok else 0)
