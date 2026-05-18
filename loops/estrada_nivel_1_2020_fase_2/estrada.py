def solve():
    C, N = map(int, input().split())
    pos = sorted(set(int(input()) for _ in range(N)))
    gaps = []
    for i in range(1, len(pos)):
        gaps.append(pos[i] - pos[i-1])
    gaps.sort(reverse=True)
    total = pos[-1] - pos[0]
    for _ in range(min(C-1, len(gaps))):
        total -= gaps[_]
    print(total)
solve()