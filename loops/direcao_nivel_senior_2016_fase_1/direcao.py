def solve():
    N, C = map(int, input().split())
    baldes = [[] for _ in range(C)]
    out = []
    for _ in range(N):
        parts = input().split()
        if parts[0] == 'I':
            v, b = int(parts[1]), int(parts[2])
            if len(baldes[b]) < 5:
                baldes[b].append(v)
        else:
            b = int(parts[1])
            if baldes[b]:
                out.append(str(max(baldes[b])))
            else:
                out.append('-1')
    print('\n'.join(out))
solve()