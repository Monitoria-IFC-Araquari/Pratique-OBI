import sys

def solve():
    data = sys.stdin.read().split()
    N, M = int(data[0]), int(data[1])
    parent = list(range(N + 1))
    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x
    def union(x, y):
        rx, ry = find(x), find(y)
        if rx != ry:
            parent[rx] = ry
    ans = 0
    for i in range(M):
        v = int(data[2 + i])
        p = find(v)
        if p == 0:
            break
        ans += 1
        union(p, p - 1)
    print(ans)

if __name__ == '__main__':
    solve()
