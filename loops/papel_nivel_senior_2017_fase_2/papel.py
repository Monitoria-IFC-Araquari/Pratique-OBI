import sys

def solve():
    n = int(sys.stdin.readline())
    a = list(map(int, sys.stdin.readline().split()))
    indices = sorted(range(n), key=lambda i: a[i], reverse=True)
    active = [False] * n
    seg = 0
    ans = 0
    i = 0
    while i < n:
        h = a[indices[i]]
        while i < n and a[indices[i]] == h:
            idx = indices[i]
            active[idx] = True
            left_act = idx > 0 and active[idx - 1]
            right_act = idx < n - 1 and active[idx + 1]
            if not left_act and not right_act:
                seg += 1
            elif left_act and right_act:
                seg -= 1
            i += 1
        if seg > ans:
            ans = seg
    print(ans)

if __name__ == '__main__':
    solve()
