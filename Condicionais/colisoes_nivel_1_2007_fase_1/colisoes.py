def solve():
    x0, y0, x1, y1 = map(int, input().split())
    x2, y2, x3, y3 = map(int, input().split())
    if x1 <= x2 or x3 <= x0 or y1 <= y2 or y3 <= y0:
        print(0)
    else:
        print(1)
solve()