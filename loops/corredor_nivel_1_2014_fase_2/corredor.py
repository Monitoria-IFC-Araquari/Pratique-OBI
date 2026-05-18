def solve():
    N = int(input())
    vals = list(map(int, input().split()))
    best = cur = vals[0]
    for v in vals[1:]:
        cur = max(v, cur + v)
        best = max(best, cur)
    print(best)
solve()