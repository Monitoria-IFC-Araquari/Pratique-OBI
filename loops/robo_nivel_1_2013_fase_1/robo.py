L, C = map(int, input().split())
A, B = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(L)]
A -= 1
B -= 1
vis = [[False] * C for _ in range(L)]
dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
while True:
    if vis[A][B]:
        break
    vis[A][B] = True
    moved = False
    for dr, dc in dirs:
        nr, nc = A + dr, B + dc
        if 0 <= nr < L and 0 <= nc < C and grid[nr][nc] == 1 and not vis[nr][nc]:
            A, B = nr, nc
            moved = True
            break
    if not moved:
        break
print(A + 1, B + 1)
