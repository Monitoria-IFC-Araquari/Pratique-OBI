def solve():
    N, L, Q = map(int, input().split())
    pos = list(map(int, input().split()))
    pos.sort()
    last = 0
    for p in pos:
        if p - last > L:
            print("N")
            return
        last = p
    print("S")
solve()