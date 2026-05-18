import sys
import bisect

def solve():
    data = sys.stdin.read().split()
    N, K = int(data[0]), int(data[1])
    a = [int(data[2 + i]) for i in range(K)]
    a.sort()
    pref = [0] * (K + 1)
    for i in range(K):
        pref[i + 1] = pref[i] + a[i]
    weather = data[2 + K:]
    delta = 0
    min_delta = 0
    total = 0
    for day in range(N):
        if weather[day] == 'C':
            delta += 1
        else:
            delta -= 1
        min_delta = min(min_delta, delta)
        threshold = -min_delta
        pos = bisect.bisect_right(a, threshold)
        cnt = K - pos
        if cnt > 0:
            total += cnt * delta + (pref[K] - pref[pos])
    print(total)

if __name__ == '__main__':
    solve()
