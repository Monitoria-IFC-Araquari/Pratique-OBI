N = int(input())
R = [int(input()) for _ in range(N)]
R.sort()
ans = 0
i, j = 0, N - 1
while i < j:
    s = R[i] + R[j]
    if s <= N:
        ans = max(ans, s)
        i += 1
    else:
        j -= 1
print(ans)
