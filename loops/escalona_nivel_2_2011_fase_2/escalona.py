def solve():
    N = int(input())
    tasks = [tuple(map(int, input().split())) for _ in range(N)]
    tasks.sort(key=lambda x: x[1])
    t = 0
    for d, p in tasks:
        t += d
        if t > p:
            print("N")
            return
    print("S")
solve()