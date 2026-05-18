def solve():
    N = int(input())
    vals = list(map(int, input().split()))
    vals.sort()
    for i in range(N-1):
        if vals[i+1] - vals[i] > 8:
            print("N")
            return
    print("S")
solve()