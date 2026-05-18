def solve():
    N = int(input())
    fila = list(map(int, input().split()))
    M = int(input())
    sai = set(map(int, input().split()))
    result = [str(x) for x in fila if x not in sai]
    print(' '.join(result))
solve()