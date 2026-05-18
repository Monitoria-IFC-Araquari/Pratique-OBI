def solve():
    c = int(input())
    a = int(input())
    viagens = (a + (c - 1) - 1) // (c - 1)
    print(viagens)

if __name__ == '__main__':
    solve()
