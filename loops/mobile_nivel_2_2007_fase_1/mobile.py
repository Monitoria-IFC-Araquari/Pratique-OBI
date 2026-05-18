import sys
sys.setrecursionlimit(20010)

n = int(input())
children = [[] for _ in range(n + 1)]
for _ in range(n):
    i, j = map(int, input().split())
    children[j].append(i)

def dfs(u):
    sz = 1
    sizes = set()
    for v in children[u]:
        sub = dfs(v)
        sizes.add(sub)
        sz += sub
    if len(sizes) > 1:
        print("mal")
        sys.exit(0)
    return sz

dfs(0)
print("bem")
