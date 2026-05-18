import sys

def solve():
    N = int(sys.stdin.readline())
    nums = list(map(int, sys.stdin.readline().split()))
    expected = N * (N + 1) // 2
    print(expected - sum(nums))

if __name__ == '__main__':
    solve()
