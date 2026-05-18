import sys

def solve():
    data = sys.stdin.read().split()
    N = int(data[0])
    sticks = sorted(int(data[i+1]) for i in range(N))
    pref = 0
    ans = 0
    for i, v in enumerate(sticks):
        if v < pref:
            ans = i + 1
        pref += v
    print(ans)

if __name__ == '__main__':
    solve()
