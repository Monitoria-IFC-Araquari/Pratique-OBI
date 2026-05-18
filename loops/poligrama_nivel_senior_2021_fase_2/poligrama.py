import sys

def solve():
    data = sys.stdin.read().split()
    N = int(data[0])
    s = data[1]
    for length in range(1, N):
        if N % length != 0:
            continue
        ref = [0] * 26
        for ch in s[:length]:
            ref[ord(ch) - 97] += 1
        ok = True
        for start in range(length, N, length):
            cur = [0] * 26
            for ch in s[start:start + length]:
                cur[ord(ch) - 97] += 1
            if cur != ref:
                ok = False
                break
        if ok:
            print(s[:length])
            return
    print('*')

if __name__ == '__main__':
    solve()
