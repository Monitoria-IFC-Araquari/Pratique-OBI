def solve():
    n = int(input())
    gab = input().strip()
    resp = input().strip()
    print(sum(1 for i in range(n) if gab[i] == resp[i]))

if __name__ == '__main__':
    solve()
