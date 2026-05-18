def solve():
    N = int(input())
    conv = [list(map(int, input().split())) for _ in range(N)]
    max1 = max(c[0] for c in conv)
    max2 = max(c[1] for c in conv)
    print(max1 + max2)
solve()