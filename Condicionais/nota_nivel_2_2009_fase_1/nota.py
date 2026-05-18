import sys

def solve():
    n = int(sys.stdin.readline())
    if n >= 86:
        print('A')
    elif n >= 61:
        print('B')
    elif n >= 36:
        print('C')
    elif n >= 1:
        print('D')
    else:
        print('E')

if __name__ == "__main__":
    solve()
