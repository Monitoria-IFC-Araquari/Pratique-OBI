def solve():
    N, K = map(int, input().split())
    labels = list(map(int, input().split()))
    count = [0]*(K+1)
    for x in labels:
        count[x] += 1
    print(min(count[1:]))
solve()