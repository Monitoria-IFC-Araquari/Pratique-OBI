import sys

def solve():
    A = int(sys.stdin.readline())
    B = int(sys.stdin.readline())
    C = int(sys.stdin.readline())
    if B - A < C - B:
        print(1)
    elif B - A > C - B:
        print(-1)
    else:
        print(0)

if __name__ == '__main__':
    solve()
