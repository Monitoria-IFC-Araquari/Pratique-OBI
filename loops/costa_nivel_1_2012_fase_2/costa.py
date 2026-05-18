def solve():
    N, M = map(int, input().split())
    g = [list(input().strip()) for _ in range(N)]
    coast = 0
    for i in range(N):
        for j in range(M):
            if g[i][j] == '#':
                if i == 0 or i == N-1 or j == 0 or j == M-1:
                    coast += 1
                else:
                    if g[i-1][j] == '.' or g[i+1][j] == '.' or g[i][j-1] == '.' or g[i][j+1] == '.':
                        coast += 1
    print(coast)
solve()