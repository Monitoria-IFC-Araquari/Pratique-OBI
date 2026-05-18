import sys

def solve():
    data = sys.stdin.read().split()
    N = int(data[0])
    subs = repair = 0
    for i in range(N):
        x = int(data[1 + i])
        if x < 50:
            subs += 1
        elif x < 85:
            repair += 1
    print(subs, repair)

if __name__ == '__main__':
    solve()
