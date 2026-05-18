def solve():
    import sys, math
    data = sys.stdin.buffer.read().split()
    it = iter(data)
    N = int(next(it))
    total = math.factorial(N)
    fact_n1 = math.factorial(N - 1)
    expected = fact_n1 * N * (N + 1) // 2
    sums = [0]*N
    for _ in range(total - 1):
        for k in range(N):
            sums[k] += int(next(it))
    missing = [str(expected - sums[k]) for k in range(N)]
    sys.stdout.write(' '.join(missing))
solve()