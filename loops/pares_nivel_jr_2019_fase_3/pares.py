import sys

def solve():
    data = sys.stdin.read().split()
    n = int(data[0]); lo = int(data[1]); hi = int(data[2])
    a = sorted(map(int, data[3:3+n]))
    ans = 0
    for i in range(n):
        left = i + 1
        right = n - 1
        while left <= right:
            mid = (left + right) // 2
            s = a[i] + a[mid]
            if s < lo:
                left = mid + 1
            else:
                right = mid - 1
        l = left
        left = i + 1
        right = n - 1
        while left <= right:
            mid = (left + right) // 2
            s = a[i] + a[mid]
            if s <= hi:
                left = mid + 1
            else:
                right = mid - 1
        r = right
        if l <= r:
            ans += r - l + 1
    print(ans)

if __name__ == '__main__':
    solve()
