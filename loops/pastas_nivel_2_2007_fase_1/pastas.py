import sys

def solve():
    data = sys.stdin.read().split()
    P, N = int(data[0]), int(data[1])
    cnt = [0] * (P + 1)
    for i in range(N):
        cnt[int(data[2 + i])] += 1
    k = min(cnt[1:])
    for i in range(1, P + 1):
        if cnt[i] != k and cnt[i] != k + 1:
            print('N')
            return
    in_prefix = True
    for i in range(1, P + 1):
        if cnt[i] == k + 1 and not in_prefix:
            print('N')
            return
        if cnt[i] == k:
            in_prefix = False
    print('S')

if __name__ == '__main__':
    solve()
