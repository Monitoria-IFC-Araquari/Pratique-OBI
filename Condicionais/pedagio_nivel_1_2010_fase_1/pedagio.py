import sys

def solve():
    L, D = map(int, sys.stdin.readline().split())
    K, P = map(int, sys.stdin.readline().split())
    print(L * K + (L // D) * P)

if __name__ == '__main__':
    solve()
