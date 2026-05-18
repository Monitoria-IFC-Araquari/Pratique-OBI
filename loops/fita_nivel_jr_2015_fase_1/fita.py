N = int(input())
fita = list(map(int, input().split()))
res = [0] * N
last_zero = -10**9
for i in range(N):
    if fita[i] == 0:
        last_zero = i
    res[i] = i - last_zero
last_zero = 10**9
for i in range(N - 1, -1, -1):
    if fita[i] == 0:
        last_zero = i
    res[i] = min(res[i], last_zero - i)
for i in range(N):
    if res[i] > 9:
        res[i] = 9
print(' '.join(map(str, res)))
