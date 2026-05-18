import sys

def solve():
    n = int(sys.stdin.readline())
    grid = [sys.stdin.readline().strip() for _ in range(n)]
    best = 0
    food = 0
    for i in range(n):
        row = grid[i]
        if i % 2 == 0:
            r = range(n)
        else:
            r = range(n - 1, -1, -1)
        for j in r:
            c = row[j]
            if c == 'o':
                food += 1
            elif c == 'A':
                food = 0
            if food > best:
                best = food
    print(best)

if __name__ == '__main__':
    solve()
