def solve():
    a, b, c = sorted(map(int, input().split()))
    if a + b <= c:
        print('n')
    else:
        a2, b2, c2 = a*a, b*b, c*c
        if a2 + b2 == c2:
            print('r')
        elif a2 + b2 > c2:
            print('a')
        else:
            print('o')

if __name__ == '__main__':
    solve()
