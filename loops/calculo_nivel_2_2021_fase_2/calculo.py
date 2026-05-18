s = int(input())
a = int(input())
b = int(input())
cnt = 0
for x in range(a, b + 1):
    ds = 0
    while x:
        ds += x % 10
        x //= 10
    if ds == s:
        cnt += 1
print(cnt)
