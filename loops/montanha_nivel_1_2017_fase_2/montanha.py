n = int(input())
a = list(map(int, input().split()))
ok = False
for i in range(1, n - 1):
    if a[i - 1] > a[i] < a[i + 1]:
        ok = True
        break
print('S' if ok else 'N')
