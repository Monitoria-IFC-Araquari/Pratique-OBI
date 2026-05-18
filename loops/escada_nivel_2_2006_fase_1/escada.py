def solve():
    N = int(input())
    h = list(map(int, input().split()))
    diff = [h[i+1]-h[i] for i in range(N-1)]
    target = diff[0]
    moves = 0
    for d in diff:
        if d != target:
            moves += abs(d - target)
    print(moves)
solve()