n = int(input())
digits = list(map(int, input().split()))

best = -1
for i in range(n):
    for j in range(n):
        if i == j:
            continue
        new = digits[:]
        new[i], new[j] = new[j], new[i]
        if new[-1] == 0 or new[-1] == 5:
            if best == -1 or new > best:
                best = new[:]

if best == -1:
    print(-1)
else:
    print(' '.join(map(str, best)))
