def solve():
    a, b, c, d = map(int, input().split())
    for x, y, z in ((a,b,c), (a,b,d), (a,c,d), (b,c,d)):
        if x + y > z and x + z > y and y + z > x:
            print('S')
            return
    print('N')

if __name__ == '__main__':
    solve()
