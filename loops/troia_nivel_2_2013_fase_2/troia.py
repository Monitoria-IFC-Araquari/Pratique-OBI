def solve():
    n, m = map(int, input().split())
    pai = list(range(n + 1))
    def find(x):
        while pai[x] != x:
            pai[x] = pai[pai[x]]
            x = pai[x]
        return x
    def union(a, b):
        a, b = find(a), find(b)
        if a != b:
            pai[b] = a
    for _ in range(m):
        a, b = map(int, input().split())
        union(a, b)
    fams = set()
    for i in range(1, n + 1):
        fams.add(find(i))
    print(len(fams))

if __name__ == '__main__':
    solve()
