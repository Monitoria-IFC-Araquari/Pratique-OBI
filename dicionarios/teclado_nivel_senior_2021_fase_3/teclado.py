def solve():
    n = input().strip()
    m = int(input())
    mapping = {
        '2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
        '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'
    }
    rev = {}
    for k, v in mapping.items():
        for c in v:
            rev[c] = k
    count = 0
    for _ in range(m):
        s = input().strip()
        if len(s) != len(n):
            continue
        ok = True
        for a, b in zip(s, n):
            if rev.get(a) != b:
                ok = False
                break
        if ok:
            count += 1
    print(count)

if __name__ == '__main__':
    solve()
