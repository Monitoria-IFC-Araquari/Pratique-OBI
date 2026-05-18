def solve():
    N = int(input())
    vals = list(map(int, input().split()))
    maior = 0
    for v in vals:
        r = int(v**0.5)
        if r*r == v and v > maior:
            maior = v
    print(maior)
solve()