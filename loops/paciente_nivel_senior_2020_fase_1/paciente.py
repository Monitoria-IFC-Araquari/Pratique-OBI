import sys

def solve():
    data = sys.stdin.read().split()
    n = int(data[0]); c = int(data[1])
    infected_by = [0] * (n + 1)
    idx = 2
    for _ in range(c):
        p = int(data[idx]); i = int(data[idx+1])
        idx += 2
        for _ in range(i):
            x = int(data[idx])
            infected_by[x] = p
            idx += 1
    zeros = [str(i) for i in range(1, n + 1) if infected_by[i] == 0]
    sys.stdout.write('\n'.join(zeros))

if __name__ == '__main__':
    solve()
