import sys

def solve():
    L = int(sys.stdin.readline())
    C = int(sys.stdin.readline())
    t1 = L * C + (L - 1) * (C - 1)
    t2 = 2 * (L + C - 2)
    print(t1)
    print(t2)

if __name__ == '__main__':
    solve()
