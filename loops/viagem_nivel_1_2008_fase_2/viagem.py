def solve():
    import sys, math
    data = list(map(int, sys.stdin.read().split()))
    n, xc, yc, r = data[0], data[1], data[2], data[3]
    count = 0
    idx = 4
    for _ in range(n):
        x1, y1, x2, y2 = data[idx], data[idx+1], data[idx+2], data[idx+3]
        idx += 4
        dx = x2 - x1
        dy = y2 - y1
        a = dx*dx + dy*dy
        b = 2 * (dx*(x1-xc) + dy*(y1-yc))
        c = (x1-xc)*(x1-xc) + (y1-yc)*(y1-yc) - r*r
        disc = b*b - 4*a*c
        if disc < 0:
            continue
        t1 = (-b - math.sqrt(disc)) / (2*a)
        t2 = (-b + math.sqrt(disc)) / (2*a)
        if (0 <= t1 <= 1) or (0 <= t2 <= 1):
            count += 1
        elif t1 < 0 and t2 > 1:
            count += 1
    print(count)

if __name__ == '__main__':
    solve()
