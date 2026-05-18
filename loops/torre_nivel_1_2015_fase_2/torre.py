def solve():
    n = int(input())
    mat = [list(map(int, input().split())) for _ in range(n)]
    row_sum = [sum(row) for row in mat]
    col_sum = [sum(mat[i][j] for i in range(n)) for j in range(n)]
    best = 0
    for i in range(n):
        for j in range(n):
            val = row_sum[i] + col_sum[j] - 2 * mat[i][j]
            if val > best:
                best = val
    print(best)

if __name__ == '__main__':
    solve()
