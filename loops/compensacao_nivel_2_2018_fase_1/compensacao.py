def solve():
    M, N = map(int, input().split())
    bal = [0]*(N+1)
    indeg = [0]*(N+1)
    outdeg = [0]*(N+1)
    for _ in range(M):
        X, V, Y = map(int, input().split())
        bal[X] -= V
        bal[Y] += V
        outdeg[X] += 1
        indeg[Y] += 1
    possible = any(indeg[i] > 0 and outdeg[i] > 0 for i in range(1, N+1))
    minimum = sum(v for v in bal if v > 0)
    print('S' if possible else 'N')
    print(minimum)
solve()