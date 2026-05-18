import sys

def solve():
    data = sys.stdin.read().split()
    N = int(data[0])
    needs = sorted([int(data[1]), int(data[2]), int(data[3])])
    ans = 0
    for x in needs:
        if N >= x:
            N -= x
            ans += 1
    print(ans)

if __name__ == '__main__':
    solve()
