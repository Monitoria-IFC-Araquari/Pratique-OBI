def solve():
    n, k = map(int, input().split())
    xs = list(map(int, input().split()))
    xs.sort()
    keep = n - k
    best = float('inf')
    for i in range(n - keep + 1):
        diff = xs[i + keep - 1] - xs[i]
        if diff < best:
            best = diff
    print(best)

if __name__ == '__main__':
    solve()
