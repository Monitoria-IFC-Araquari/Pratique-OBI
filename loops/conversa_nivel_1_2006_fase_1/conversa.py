def solve():
    N, M = map(int, input().split())
    X, Y = map(int, input().split())
    K = int(input())
    dirs = list(map(int, input().split()))
    x, y = 0, 0
    count = 0
    for d in dirs:
        if d == 1:
            x += 1
        elif d == 2:
            x -= 1
        elif d == 3:
            y += 1
        else:
            y -= 1
        if abs(x-X) <= 1 and abs(y-Y) <= 1:
            count += 1
    print(count)
solve()