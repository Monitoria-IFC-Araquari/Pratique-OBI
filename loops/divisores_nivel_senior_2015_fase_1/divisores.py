def solve():
    N = int(input())
    vals = list(map(int, input().split()))
    for v in vals:
        divs = []
        for d in range(1, int(v**0.5)+1):
            if v % d == 0:
                divs.append(d)
                if d*d != v:
                    divs.append(v//d)
        divs.sort()
        print(' '.join(map(str, divs)))
solve()