N, M = map(int, input().split())
parent = list(range(N + 1))
def find(x):
    while parent[x] != x:
        parent[x] = parent[parent[x]]
        x = parent[x]
    return x
def union(a, b):
    a, b = find(a), find(b)
    if a != b:
        parent[a] = b
for _ in range(M):
    I, J = map(int, input().split())
    union(I, J)
groups = set()
for i in range(1, N + 1):
    groups.add(find(i))
print(len(groups))
