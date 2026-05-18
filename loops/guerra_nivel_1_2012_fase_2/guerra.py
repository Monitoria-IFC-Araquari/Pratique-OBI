N = int(input())
a = list(map(int, input().split()))
total = sum(a)
s = 0
for i in range(N):
    s += a[i]
    if s * 2 == total:
        print(i + 1)
        break
