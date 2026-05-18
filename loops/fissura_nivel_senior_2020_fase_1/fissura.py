def solve():
    N, F = map(int, input().split())
    grid = [list(input().strip()) for _ in range(N)]
    if int(grid[0][0]) > F:
        for line in grid:
            print(''.join(line))
        return
    from collections import deque
    q = deque([(0, 0)])
    grid[0][0] = '*'
    dirs = [(1,0),(-1,0),(0,1),(0,-1)]
    while q:
        x, y = q.popleft()
        for dx, dy in dirs:
            nx, ny = x+dx, y+dy
            if 0 <= nx < N and 0 <= ny < N and grid[nx][ny] != '*' and int(grid[nx][ny]) <= F:
                grid[nx][ny] = '*'
                q.append((nx, ny))
    for line in grid:
        print(''.join(line))
solve()