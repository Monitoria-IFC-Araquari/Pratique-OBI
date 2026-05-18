N, M = map(int, input().split())
mat = [[0] * (N + 1) for _ in range(N + 1)]
for _ in range(M):
    X, Y, Z = map(int, input().split())
    mat[X][Y] = Z
    mat[Y][X] = Z

best = -1
best_trio = (0, 0, 0)
for i in range(1, N + 1):
    for j in range(i + 1, N + 1):
        for k in range(j + 1, N + 1):
            s = mat[i][j] + mat[i][k] + mat[j][k]
            if s > best:
                best = s
                best_trio = (i, j, k)
print(*best_trio)
