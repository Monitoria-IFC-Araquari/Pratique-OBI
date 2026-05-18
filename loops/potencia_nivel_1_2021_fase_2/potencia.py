import sys

def solve():
    data = sys.stdin.read().split()
    N = int(data[0])
    total = 0
    for i in range(N):
        T = int(data[1 + i])
        total += (T // 10) ** (T % 10)
    print(total)

if __name__ == '__main__':
    solve()
