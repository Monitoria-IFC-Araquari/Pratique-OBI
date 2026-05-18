import sys

def exp2(x):
    c = 0
    while x % 2 == 0:
        x //= 2
        c += 1
    return c

def exp5(x):
    c = 0
    while x % 5 == 0:
        x //= 5
        c += 1
    return c

def solve():
    data = sys.stdin.read().split()
    N = int(data[0])
    INF = 10 ** 9
    dp2 = [[INF] * N for _ in range(N)]
    dp5 = [[INF] * N for _ in range(N)]
    idx = 1
    for i in range(N):
        for j in range(N):
            v = int(data[idx]); idx += 1
            if v == 0:
                continue
            a2 = exp2(v)
            a5 = exp5(v)
            if i == 0 and j == 0:
                dp2[i][j] = a2
                dp5[i][j] = a5
            else:
                if i > 0:
                    dp2[i][j] = min(dp2[i][j], dp2[i-1][j] + a2)
                    dp5[i][j] = min(dp5[i][j], dp5[i-1][j] + a5)
                if j > 0:
                    dp2[i][j] = min(dp2[i][j], dp2[i][j-1] + a2)
                    dp5[i][j] = min(dp5[i][j], dp5[i][j-1] + a5)
    print(min(dp2[N-1][N-1], dp5[N-1][N-1]))

if __name__ == '__main__':
    solve()
