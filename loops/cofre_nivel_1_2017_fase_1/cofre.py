n, m = map(int, input().split())
barra = list(map(int, input().split()))
pos = list(map(int, input().split()))
diff = [0] * (n + 2)
diff[1] += 1
diff[2] -= 1
for i in range(1, m):
    a, b = pos[i-1], pos[i]
    if a < b:
        diff[a+1] += 1
        diff[b+1] -= 1
    else:
        diff[b] += 1
        diff[a] -= 1
freq = [0] * 10
cnt = 0
for i in range(1, n + 1):
    cnt += diff[i]
    freq[barra[i-1]] += cnt
print(' '.join(map(str, freq)))
