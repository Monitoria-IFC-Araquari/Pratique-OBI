import sys
import bisect

def solve():
    data = sys.stdin.read().split()
    it = iter(data)
    N = int(next(it)); M = int(next(it))
    faixas = [int(next(it)) for _ in range(N - 1)]
    premios = [int(next(it)) for _ in range(N)]
    ogros = [int(next(it)) for _ in range(M)]
    out = []
    for f in ogros:
        idx = bisect.bisect_left(faixas, f)
        out.append(str(premios[idx]))
    sys.stdout.write(' '.join(out))

if __name__ == '__main__':
    solve()
