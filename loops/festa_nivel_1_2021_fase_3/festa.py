def solve():
    N = int(input())
    conv = [list(map(int, input().split())) for _ in range(N)]
    total = 0
    for i in range(N):
        for j in range(N):
            if j != i:
                total = max(total, conv[i][0] + conv[j][1])
    print(total)
solve()