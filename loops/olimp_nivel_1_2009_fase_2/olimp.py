import sys

def solve():
    data = sys.stdin.read().split()
    n = int(data[0]); m = int(data[1])
    medals = [[0, 0, 0, i] for i in range(n)]
    idx = 2
    for _ in range(m):
        o = int(data[idx]); p = int(data[idx+1]); b = int(data[idx+2])
        medals[o-1][0] += 1
        medals[p-1][1] += 1
        medals[b-1][2] += 1
        idx += 3
    medals.sort(key=lambda x: (-x[0], -x[1], -x[2], x[3]))
    print(' '.join(str(m[3]+1) for m in medals))

if __name__ == '__main__':
    solve()
