import sys

def solve():
    n = int(sys.stdin.readline())
    a = list(map(int, sys.stdin.readline().split()))
    if n <= 2:
        print(1)
        return
    ans = 1
    r = a[1] - a[0]
    for i in range(2, n):
        if a[i] - a[i-1] != r:
            ans += 1
            r = a[i] - a[i-1]
    print(ans)

if __name__ == '__main__':
    solve()
