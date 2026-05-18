def solve():
    N, C, M = map(int, input().split())
    carimbadas = set(map(int, input().split()))
    compradas = set(map(int, input().split()))
    print(len(carimbadas - compradas))
solve()