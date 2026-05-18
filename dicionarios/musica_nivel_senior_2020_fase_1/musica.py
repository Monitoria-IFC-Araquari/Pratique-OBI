import sys

def solve():
    data = sys.stdin.read().split()
    if not data:
        return
    it = iter(data)
    N = int(next(it))
    M = int(next(it))
    C = int(next(it))

    first_hater = {}
    adored = {}
    for i in range(N):
        a = int(next(it))
        d = int(next(it))
        if d not in first_hater:
            first_hater[d] = i
            adored[d] = a

    next_music = {}
    for d, idx in first_hater.items():
        next_music[d] = adored[d]

    visited = set()
    cur = C
    count = 0
    while cur in next_music:
        if cur in visited:
            print(-1)
            return
        visited.add(cur)
        cur = next_music[cur]
        count += 1
    print(count)

if __name__ == "__main__":
    solve()
