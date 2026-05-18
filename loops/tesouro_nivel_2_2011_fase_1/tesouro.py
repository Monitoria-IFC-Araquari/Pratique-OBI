def solve():
    n, k = map(int, input().split())
    pistas = []
    for _ in range(k):
        x, y, d = map(int, input().split())
        pistas.append((x, y, d))
    candidates = []
    for x in range(n):
        for y in range(n):
            ok = True
            for px, py, d in pistas:
                if abs(x - px) + abs(y - py) != d:
                    ok = False
                    break
            if ok:
                candidates.append((x, y))
    if len(candidates) == 1:
        print(candidates[0][0], candidates[0][1])
    else:
        print(-1, -1)

if __name__ == '__main__':
    solve()
