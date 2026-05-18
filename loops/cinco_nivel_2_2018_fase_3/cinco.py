n = int(input())
digits = list(map(int, input().split()))

pos5 = [i for i, d in enumerate(digits) if d == 5]
pos0 = [i for i, d in enumerate(digits) if d == 0]

best = -1
best_i = best_j = -1

for i in range(n):
    for j in range(n):
        if i == j:
            continue
        new = digits[:]
        new[i], new[j] = new[j], new[i]
        if new[-1] == 0 or new[-1] == 5:
            if best == -1 or new > best:
                best = new[:]
                best_i, best_j = i, j

if best == -1:
    print(-1)
else:
    print(' '.join(map(str, best)))
