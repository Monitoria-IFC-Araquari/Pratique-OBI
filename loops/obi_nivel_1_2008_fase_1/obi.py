import sys

def solve():
    data = sys.stdin.read().split()
    n = int(data[0])
    p = int(data[1])
    ans = 0
    for i in range(n):
        x = int(data[2 + 2*i])
        y = int(data[3 + 2*i])
        if x + y >= p:
            ans += 1
    print(ans)

if __name__ == "__main__":
    solve()
