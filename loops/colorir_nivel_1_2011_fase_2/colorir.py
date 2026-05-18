def solve():
    import sys
    sys.setrecursionlimit(1000000)
    N, M, X, Y, K = map(int, input().split())
    blocked = [[False]*(M+1) for _ in range(N+1)]
    for _ in range(K):
        a, b = map(int, input().split())
        blocked[a][b] = True
    blocked[X][Y] = True
    stack = [(X, Y)]
    count = 1
    dirs = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]
    while stack:
        x, y = stack.pop()
        for dx, dy in dirs:
            nx, ny = x+dx, y+dy
            if 1 <= nx <= N and 1 <= ny <= M and not blocked[nx][ny]:
                blocked[nx][ny] = True
                stack.append((nx, ny))
                count += 1
    print(count)
solve()