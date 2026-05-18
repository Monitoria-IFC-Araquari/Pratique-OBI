n, m = map(int, input().split())
a = list(map(int, input().split()))
ops = list(map(int, input().split()))

diff = [0] * (n + 2)

for i in ops:
    i -= 1
    c = a[i]
    if c == 0:
        continue
    l = max(0, i - c)
    r = min(n - 1, i + c)
    diff[l] += 1
    diff[r + 1] -= 1

cur = 0
for i in range(n):
    cur += diff[i]
    if cur > a[i]:
        a[i] = 0
    else:
        a[i] -= cur

print(sum(a))
