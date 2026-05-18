def solve():
    N = int(input())
    vals = list(map(int, input().split()))
    vals.sort()
    i, j = 0, len(vals)-1
    total = 0
    while i < j:
        total += vals[j] - vals[i]
        i += 1
        j -= 1
    print(total)
solve()