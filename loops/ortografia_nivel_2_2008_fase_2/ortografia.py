import sys

def dist_le2(a, b):
    la, lb = len(a), len(b)
    if abs(la - lb) > 2:
        return False
    if a == b:
        return True
    dp = list(range(lb + 1))
    for i in range(1, la + 1):
        prev = dp[0]
        dp[0] = i
        start = max(1, i - 2)
        end = min(lb, i + 2)
        for j in range(1, start):
            dp[j] = lb + 1
        for j in range(start, end + 1):
            temp = dp[j]
            if a[i-1] == b[j-1]:
                dp[j] = prev
            else:
                dp[j] = 1 + min(prev, dp[j], dp[j-1])
            prev = temp
        for j in range(end + 1, lb + 1):
            dp[j] = lb + 1
    return dp[lb] <= 2

def solve():
    data = sys.stdin.read().splitlines()
    n, m = map(int, data[0].split())
    dic = data[1:1+n]
    out_lines = []
    for i in range(m):
        word = data[1+n+i]
        matches = []
        for j, d in enumerate(dic):
            if dist_le2(word, d):
                matches.append(d)
        out_lines.append(' '.join(matches))
    sys.stdout.write('\n'.join(out_lines))

if __name__ == '__main__':
    solve()
