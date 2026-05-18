def solve():
    import sys
    ordem = {4:0, 5:1, 6:2, 7:3, 12:4, 11:5, 13:6, 1:7, 2:8, 3:9}
    data = sys.stdin.read().strip().split()
    if not data:
        return
    n = int(data[0])
    win_a = 0
    win_b = 0
    idx = 1
    for _ in range(n):
        a = list(map(int, data[idx:idx+3]))
        b = list(map(int, data[idx+3:idx+6]))
        idx += 6
        ra, rb = 0, 0
        for i in range(3):
            va = ordem[a[i]]
            vb = ordem[b[i]]
            if va >= vb:
                ra += 1
            else:
                rb += 1
        if ra > rb:
            win_a += 1
        else:
            win_b += 1
    print(win_a, win_b)

if __name__ == '__main__':
    solve()
