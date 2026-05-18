import sys

def solve():
    s = sys.stdin.readline().strip()
    val = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    n = len(s)
    stack = []
    i = 0
    total = 0
    while i < n:
        v = val[s[i]]
        j = i + 1
        while j < n and val[s[j]] > val[s[i]]:
            v -= val[s[j]]
            j += 1
        total += v
        i = j
    print(total)

if __name__ == "__main__":
    solve()
