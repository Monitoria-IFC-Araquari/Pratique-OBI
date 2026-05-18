import sys

def solve():
    data = sys.stdin.read().split()
    N = int(data[0])
    arr = [int(data[i+1]) for i in range(N)]
    max_ending = cur = 0
    for v in arr:
        cur = max(0, cur + v)
        max_ending = max(max_ending, cur)
    total = sum(arr)
    min_ending = cur_min = 0
    for v in arr:
        cur_min = min(0, cur_min + v)
        min_ending = min(min_ending, cur_min)
    ans = max(max_ending, total - min_ending)
    print(ans)

if __name__ == '__main__':
    solve()
