L, C = map(int, input().split())
grid = [list(input().strip()) for _ in range(L)]

for i in range(L):
    for j in range(C):
        if grid[i][j] == 'o':
            si, sj = i, j
            break

i, j = si, sj
prev_i, prev_j = -1, -1
while True:
    found_next = False
    for di, dj in ((1, 0), (-1, 0), (0, 1), (0, -1)):
        ni, nj = i + di, j + dj
        if 0 <= ni < L and 0 <= nj < C and grid[ni][nj] == 'H' and (ni, nj) != (prev_i, prev_j):
            prev_i, prev_j = i, j
            i, j = ni, nj
            found_next = True
            break
    if not found_next:
        print(i + 1, j + 1)
        break
