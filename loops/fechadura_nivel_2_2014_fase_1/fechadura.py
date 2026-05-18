def solve():
    N, M = map(int, input().split())
    h = list(map(int, input().split()))
    moves = 0
    for i in range(N-1):
        diff = M - h[i]
        h[i] += diff
        h[i+1] += diff
        moves += abs(diff)
    print(moves)
solve()