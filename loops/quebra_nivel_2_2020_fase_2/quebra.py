N = int(input())
grid = [list(map(int, input().split())) for _ in range(2)]
empty = (0, 0)
for i in range(2):
    for j in range(N):
        if grid[i][j] == 0:
            empty = (i, j)
ans = 0
target = 1
while target < N:
    for i in range(2):
        for j in range(N):
            if grid[i][j] == target:
                while empty != (i, j):
                    ei, ej = empty
                    if ei == i:
                        if ej < j:
                            grid[ei][ej] = grid[ei][ej + 1]
                            grid[ei][ej + 1] = 0
                            empty = (ei, ej + 1)
                        else:
                            grid[ei][ej] = grid[ei][ej - 1]
                            grid[ei][ej - 1] = 0
                            empty = (ei, ej - 1)
                    else:
                        grid[ei][ej] = grid[1 - ei][ej]
                        grid[1 - ei][ej] = 0
                        empty = (1 - ei, ej)
                    ans += 1
                target += 1
                break
        else:
            continue
        break
print(ans)
