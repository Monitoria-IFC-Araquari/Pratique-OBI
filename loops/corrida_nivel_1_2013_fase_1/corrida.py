def solve():
    N, M = map(int, input().split())
    best = float('inf')
    winner = 0
    for i in range(1, N+1):
        laps = list(map(int, input().split()))
        t = sum(laps)
        if t < best:
            best = t
            winner = i
    print(winner)
solve()