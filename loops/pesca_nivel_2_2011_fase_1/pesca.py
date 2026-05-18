import sys

def solve():
    data = sys.stdin.read().split()
    N = int(data[0])
    grid = [[False] * 101 for _ in range(101)]
    idx = 1
    for _ in range(N):
        xi = int(data[idx]); xf = int(data[idx+1])
        yi = int(data[idx+2]); yf = int(data[idx+3])
        idx += 4
        for x in range(xi, xf + 1):
            for y in range(yi, yf + 1):
                grid[x][y] = True
    ans = sum(sum(row) for row in grid)
    print(ans)

if __name__ == '__main__':
    solve()
