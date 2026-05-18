N = int(input())
L = list(map(int, input().split()))
pos = {L[i]: i for i in range(N)}
ans = 0
for i in range(N):
    for j in range(i + 1, N):
        d1 = L[i] + L[j]
        if d1 % 2 != 0:
            continue
        need = d1 // 2
        if need in pos:
            k = pos[need]
            if k != i and k != j:
                d2 = abs(L[i] - L[j])
                if d2 in pos and d2 != need:
                    l = pos[d2]
                    if l != i and l != j and l != k:
                        ans = max(ans, d1 + d2)
print(ans)
