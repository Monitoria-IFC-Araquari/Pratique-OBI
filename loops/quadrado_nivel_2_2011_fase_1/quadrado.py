N, S = map(int, input().split())
for i in range(N):
    row = []
    for j in range(N):
        if i == j:
            row.append(str(S))
        elif j == N - 1 - i:
            row.append(str(0))
        else:
            row.append(str(0))
    print(' '.join(row))
