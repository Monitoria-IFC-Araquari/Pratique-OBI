m, n = map(int, input().split())
x = list(map(int, input().split()))
y = list(map(int, input().split()))

size = max(m, n) + 1
a = [0] * size
b = [0] * size
for i in range(m):
    a[size - m + i] = x[i]
for i in range(n):
    b[size - n + i] = y[i]

res = [0] * size
carry = 0
for i in range(size - 1, -1, -1):
    s = a[i] + b[i] + carry
    res[i] = s % 2
    carry = s // 2

while len(res) > 1 and res[-1] == 0:
    res.pop()

print(' '.join(map(str, res)))
