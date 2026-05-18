n = int(input())
a = list(map(int, input().split()))
i, j = 0, n - 1
ans = 0
while i < j:
    if a[i] == a[j]:
        i += 1
        j -= 1
    elif a[i] < a[j]:
        a[i + 1] += a[i]
        i += 1
        ans += 1
    else:
        a[j - 1] += a[j]
        j -= 1
        ans += 1
print(ans)
