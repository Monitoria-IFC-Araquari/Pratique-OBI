def solve():
    N, M = map(int, input().split())
    mat = [list(map(int, input().split())) for _ in range(N)]
    pivot_col = -1
    for i in range(N):
        first = -1
        for j in range(M):
            if mat[i][j] != 0:
                first = j
                break
        if first == -1:
            for k in range(i+1, N):
                if any(mat[k][j] != 0 for j in range(M)):
                    print("N")
                    return
            continue
        if first <= pivot_col:
            print("N")
            return
        pivot_col = first
    print("S")
solve()